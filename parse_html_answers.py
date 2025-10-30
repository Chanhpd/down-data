from bs4 import BeautifulSoup
import json
import re

def parse_answers_from_html(html_file):
    """Parse correct answers from submitted quiz HTML"""
    
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    answers = {}
    question_num = 0
    
    # Find all question blocks with class 'show-question'
    question_divs = soup.find_all('div', class_='show-question')
    
    print(f"📝 Found {len(question_divs)} question blocks\n")
    
    for question_div in question_divs:
        question_num += 1
        
        # Find the correct answer within this question
        correct_li = question_div.find('li', class_='correct-answer')
        
        if correct_li:
            answer_span = correct_li.find('span', class_='answer')
            if answer_span:
                answer = answer_span.text.strip()
                answers[question_num] = answer
                print(f"Q{question_num}: {answer}")
        else:
            print(f"Q{question_num}: ⚠️  No correct answer found")
    
    return answers

def update_json_with_answers(answers, json_file='H20901_complete.json'):
    """Update JSON file with parsed answers"""
    
    with open(json_file, 'r', encoding='utf-8') as f:
        exam = json.load(f)
    
    updated_count = 0
    
    # Update listening section (Q1-Q35)
    listening = exam['sections'][0]
    for part in listening['parts']:
        # Handle sub_parts (Part 2)
        if 'sub_parts' in part and part['sub_parts']:
            for sub_part in part['sub_parts']:
                for question in sub_part['questions']:
                    q_num = question['question_number']
                    if q_num in answers:
                        question['correct_answer'] = answers[q_num]
                        updated_count += 1
        else:
            # Regular questions
            for question in part.get('questions', []):
                q_num = question['question_number']
                if q_num in answers:
                    question['correct_answer'] = answers[q_num]
                    updated_count += 1
    
    # Save updated file
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(exam, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Updated {updated_count} answers in {json_file}")
    return updated_count

if __name__ == "__main__":
    print("="*60)
    print("Parsing H20901 Listening Answers from HTML")
    print("="*60 + "\n")
    
    # Parse answers from HTML
    html_file = "H20901 Listening - Mandarin Bean.html"
    answers = parse_answers_from_html(html_file)
    
    print(f"\n{'='*60}")
    print(f"Total answers found: {len(answers)}")
    print("="*60)
    
    if answers:
        # Update JSON
        updated = update_json_with_answers(answers)
        
        print(f"\n🎉 Success! Updated {updated} listening answers")
        print("\n📋 Answer Summary:")
        print(f"   Q1-Q10 (Part 1): {[answers.get(i, '?') for i in range(1, 11)]}")
        print(f"   Q11-Q15 (Part 2): {[answers.get(i, '?') for i in range(11, 16)]}")
        print(f"   Q16-Q20 (Part 2): {[answers.get(i, '?') for i in range(16, 21)]}")
        
        if 21 in answers:
            print(f"   Q21-Q25: {[answers.get(i, '?') for i in range(21, 26)]}")
        if 26 in answers:
            print(f"   Q26-Q30 (Part 3): {[answers.get(i, '?') for i in range(26, 31)]}")
        if 31 in answers:
            print(f"   Q31-Q35 (Part 4): {[answers.get(i, '?') for i in range(31, 36)]}")
    else:
        print("\n❌ No answers found!")
