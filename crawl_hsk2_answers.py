from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import time

def crawl_hsk2_answers():
    """Crawl HSK 2 answers by clicking View Result button"""
    
    # Setup Chrome options
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Run in background
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # Initialize driver
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        print("🌐 Loading H20901 Listening page...")
        driver.get("https://mandarinbean.com/h20901-listening/")
        
        # Wait for page to load
        time.sleep(3)
        
        # Find and click "View Result" or submit button
        # Common button selectors on quiz sites
        possible_buttons = [
            "//button[contains(text(), 'View Result')]",
            "//button[contains(text(), 'Show Answers')]",
            "//a[contains(text(), 'View Result')]",
            "//input[@type='submit']",
            "//button[@type='submit']",
            ".watupro-submit",
            "#watupro_submit"
        ]
        
        button_clicked = False
        for selector in possible_buttons:
            try:
                if selector.startswith("//"):
                    button = driver.find_element(By.XPATH, selector)
                elif selector.startswith("."):
                    button = driver.find_element(By.CSS_SELECTOR, selector)
                else:
                    button = driver.find_element(By.CSS_SELECTOR, selector)
                
                print(f"✅ Found button: {selector}")
                button.click()
                button_clicked = True
                time.sleep(3)
                break
            except Exception as e:
                continue
        
        if not button_clicked:
            print("⚠️  No submit button found, trying to find answers in page source...")
        
        # Try to find correct answers in the page
        # Pattern 1: Look for correct answer indicators
        answers = {}
        
        # Method 1: Find elements with correct answer class
        try:
            correct_elements = driver.find_elements(By.CSS_SELECTOR, ".watupro-correct, .correct-answer, .answer.correct")
            print(f"📝 Found {len(correct_elements)} correct answer elements")
        except:
            pass
        
        # Method 2: Look for answer key in page source
        page_source = driver.page_source
        
        # Save page source for inspection
        with open('h20901_listening_page.html', 'w', encoding='utf-8') as f:
            f.write(page_source)
        print("💾 Saved page source to h20901_listening_page.html")
        
        # Method 3: Try to find answer patterns in HTML
        # Pattern: data-correct="A" or similar
        import re
        
        # Look for patterns like: correct answer is A, B, TRUE, FALSE, etc.
        answer_patterns = [
            r'data-correct="([A-F]|TRUE|FALSE)"',
            r'data-answer="([A-F]|TRUE|FALSE)"',
            r'correct[_-]?answer["\s:]+([A-F]|TRUE|FALSE)',
            r'"correct":\s*"([A-F]|TRUE|FALSE)"'
        ]
        
        for pattern in answer_patterns:
            matches = re.findall(pattern, page_source, re.IGNORECASE)
            if matches:
                print(f"✅ Found {len(matches)} answers with pattern: {pattern}")
                for i, answer in enumerate(matches, 1):
                    answers[i] = answer.upper()
                break
        
        if answers:
            print(f"\n📋 Found {len(answers)} answers:")
            for q, ans in sorted(answers.items()):
                print(f"   Q{q}: {ans}")
        else:
            print("\n⚠️  No answers found automatically.")
            print("Please check h20901_listening_page.html manually")
            print("Or try clicking View Result button manually in the browser")
        
        # Keep browser open for manual inspection
        input("\n⏸️  Press Enter to close browser...")
        
        return answers
        
    finally:
        driver.quit()

def update_json_with_answers(answers_listening, answers_reading=None):
    """Update H20901_complete.json with correct answers"""
    
    with open('H20901_complete.json', 'r', encoding='utf-8') as f:
        exam = json.load(f)
    
    # Update listening answers
    listening = exam['sections'][0]
    for part in listening['parts']:
        if 'sub_parts' in part and part['sub_parts']:
            for sub_part in part['sub_parts']:
                for question in sub_part['questions']:
                    q_num = question['question_number']
                    if q_num in answers_listening:
                        question['correct_answer'] = answers_listening[q_num]
        else:
            for question in part.get('questions', []):
                q_num = question['question_number']
                if q_num in answers_listening:
                    question['correct_answer'] = answers_listening[q_num]
    
    # Update reading answers if provided
    if answers_reading:
        reading = exam['sections'][1]
        for part in reading['parts']:
            for question in part['questions']:
                q_num = question['question_number']
                if q_num in answers_reading:
                    question['correct_answer'] = answers_reading[q_num]
    
    # Save updated file
    with open('H20901_complete.json', 'w', encoding='utf-8') as f:
        json.dump(exam, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Updated H20901_complete.json with {len(answers_listening)} listening answers")
    if answers_reading:
        print(f"✅ Updated with {len(answers_reading)} reading answers")

if __name__ == "__main__":
    print("="*60)
    print("HSK 2 H20901 Answer Crawler")
    print("="*60)
    
    # Crawl listening answers
    listening_answers = crawl_hsk2_answers()
    
    if listening_answers:
        # Update JSON file
        update_json_with_answers(listening_answers)
    else:
        print("\n❌ No answers found. Please:")
        print("   1. Check h20901_listening_page.html")
        print("   2. Manually click 'View Result' in browser")
        print("   3. Inspect the answer format")
        print("   4. Update the regex patterns in the script")
