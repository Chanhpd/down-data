from bs4 import BeautifulSoup
import json
import re

def parse_reading_answers(html_file):
    """Parse correct answers from Reading HTML"""
    
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    answers = {}
    question_num = 35  # Reading starts from Q36
    
    # Find all question blocks with class 'show-question'
    question_divs = soup.find_all('div', class_='show-question')
    
    print(f"📝 Found {len(question_divs)} reading question blocks\n")
    
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

def update_json_with_reading_answers(answers, json_file='H20901_complete.json'):
    """Update JSON file with reading answers"""
    
    with open(json_file, 'r', encoding='utf-8') as f:
        exam = json.load(f)
    
    updated_count = 0
    
    # Update reading section (Q36-Q60)
    reading = exam['sections'][1]
    for part in reading['parts']:
        for question in part['questions']:
            q_num = question['question_number']
            if q_num in answers:
                question['correct_answer'] = answers[q_num]
                updated_count += 1
    
    # Save updated file
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(exam, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Updated {updated_count} reading answers in {json_file}")
    return updated_count

if __name__ == "__main__":
    print("="*60)
    print("Parsing H20901 Reading Answers from HTML")
    print("="*60 + "\n")
    
    # Parse answers from HTML
    html_file = "H20901 Reading - Mandarin Bean.html"
    answers = parse_reading_answers(html_file)
    
    print(f"\n{'='*60}")
    print(f"Total reading answers found: {len(answers)}")
    print("="*60)
    
    if answers:
        # Update JSON
        updated = update_json_with_reading_answers(answers)
        
        print(f"\n🎉 Success! Updated {updated} reading answers")
        print("\n📋 Answer Summary:")
        print(f"   Q36-Q40 (Part 1): {[answers.get(i, '?') for i in range(36, 41)]}")
        print(f"   Q41-Q45 (Part 2): {[answers.get(i, '?') for i in range(41, 46)]}")
        print(f"   Q46-Q50 (Part 3): {[answers.get(i, '?') for i in range(46, 51)]}")
        print(f"   Q51-Q55 (Part 4): {[answers.get(i, '?') for i in range(51, 56)]}")
        print(f"   Q56-Q60 (Part 4): {[answers.get(i, '?') for i in range(56, 61)]}")
    else:
        print("\n❌ No answers found!")
