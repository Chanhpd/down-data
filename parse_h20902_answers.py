from bs4 import BeautifulSoup
import json

def parse_h20902_answers(html_file, section_type):
    """Parse answers from H20902 HTML"""
    
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    answers = {}
    
    # Determine starting question number
    if section_type == 'listening':
        question_num = 0  # Q1-Q35
    else:  # reading
        question_num = 35  # Q36-Q60
    
    question_divs = soup.find_all('div', class_='show-question')
    
    print(f"📝 Found {len(question_divs)} {section_type} questions\n")
    
    for question_div in question_divs:
        question_num += 1
        
        correct_li = question_div.find('li', class_='correct-answer')
        
        if correct_li:
            answer_span = correct_li.find('span', class_='answer')
            if answer_span:
                answer = answer_span.text.strip()
                answers[question_num] = answer
                print(f"Q{question_num}: {answer}")
        else:
            print(f"Q{question_num}: ⚠️  No answer found")
    
    return answers

def update_json(listening_answers, reading_answers):
    """Update H20902_complete.json with answers"""
    
    with open('H20902_complete.json', 'r', encoding='utf-8') as f:
        exam = json.load(f)
    
    updated = 0
    
    # Update listening
    listening = exam['sections'][0]
    for part in listening['parts']:
        if 'sub_parts' in part and part['sub_parts']:
            for sub_part in part['sub_parts']:
                for question in sub_part['questions']:
                    q_num = question['question_number']
                    if q_num in listening_answers:
                        question['correct_answer'] = listening_answers[q_num]
                        updated += 1
        else:
            for question in part.get('questions', []):
                q_num = question['question_number']
                if q_num in listening_answers:
                    question['correct_answer'] = listening_answers[q_num]
                    updated += 1
    
    # Update reading
    reading = exam['sections'][1]
    for part in reading['parts']:
        for question in part['questions']:
            q_num = question['question_number']
            if q_num in reading_answers:
                question['correct_answer'] = reading_answers[q_num]
                updated += 1
    
    with open('H20902_complete.json', 'w', encoding='utf-8') as f:
        json.dump(exam, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Updated {updated} answers in H20902_complete.json")

if __name__ == "__main__":
    print("="*60)
    print("H20902 Answer Parser")
    print("="*60)
    print()
    print("⚠️  Instructions:")
    print("1. Go to: https://mandarinbean.com/h20902-listening/")
    print("2. Click 'View Result' button")
    print("3. Save page as: H20902 Listening - Mandarin Bean.html")
    print()
    print("4. Go to: https://mandarinbean.com/h20902-reading/")
    print("5. Click 'View Result' button")
    print("6. Save page as: H20902 Reading - Mandarin Bean.html")
    print()
    print("7. Run this script again")
    print("="*60)
    
    import os
    listening_file = "H20902 Listening - Mandarin Bean.html"
    reading_file = "H20902 Reading - Mandarin Bean.html"
    
    if os.path.exists(listening_file) and os.path.exists(reading_file):
        print("\n✅ Found HTML files, parsing...\n")
        
        listening_ans = parse_h20902_answers(listening_file, 'listening')
        print(f"\nListening: {len(listening_ans)} answers")
        
        reading_ans = parse_h20902_answers(reading_file, 'reading')
        print(f"Reading: {len(reading_ans)} answers")
        
        update_json(listening_ans, reading_ans)
        
        print("\n🎉 Done! Check H20902_complete.json")
    else:
        print("\n⚠️  HTML files not found. Please follow instructions above.")
