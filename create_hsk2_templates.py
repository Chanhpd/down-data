import json
import shutil

def create_hsk2_exam_template(exam_id):
    """Create HSK 2 exam template based on H20901"""
    
    # Load H20901 as template
    with open('H20901_complete.json', 'r', encoding='utf-8') as f:
        template = json.load(f)
    
    # Update exam info
    template['exam_id'] = exam_id
    template['exam_title'] = f"HSK Level 2 - {exam_id} Complete Exam"
    
    # Update URLs
    template['sections'][0]['exam_url'] = f"https://mandarinbean.com/{exam_id.lower()}-listening/"
    template['sections'][0]['audio_file'] = f"https://traffic.libsyn.com/secure/learnchinese/{exam_id}.mp3"
    template['sections'][1]['exam_url'] = f"https://mandarinbean.com/{exam_id.lower()}-reading/"
    
    # Clear all answers (keep structure)
    def clear_answers(obj):
        if isinstance(obj, dict):
            if 'correct_answer' in obj:
                obj['correct_answer'] = ""
            for value in obj.values():
                clear_answers(value)
        elif isinstance(obj, list):
            for item in obj:
                clear_answers(item)
    
    clear_answers(template)
    
    # Save template
    output_file = f"{exam_id}_complete.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(template, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Created {output_file}")
    return output_file

def create_html_parser_for_exam(exam_id):
    """Create parser script for specific exam"""
    
    script_content = f'''from bs4 import BeautifulSoup
import json

def parse_{exam_id.lower()}_answers(html_file, section_type):
    """Parse answers from {exam_id} HTML"""
    
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    answers = {{}}
    
    # Determine starting question number
    if section_type == 'listening':
        question_num = 0  # Q1-Q35
    else:  # reading
        question_num = 35  # Q36-Q60
    
    question_divs = soup.find_all('div', class_='show-question')
    
    print(f"📝 Found {{len(question_divs)}} {{section_type}} questions\\n")
    
    for question_div in question_divs:
        question_num += 1
        
        correct_li = question_div.find('li', class_='correct-answer')
        
        if correct_li:
            answer_span = correct_li.find('span', class_='answer')
            if answer_span:
                answer = answer_span.text.strip()
                answers[question_num] = answer
                print(f"Q{{question_num}}: {{answer}}")
        else:
            print(f"Q{{question_num}}: ⚠️  No answer found")
    
    return answers

def update_json(listening_answers, reading_answers):
    """Update {exam_id}_complete.json with answers"""
    
    with open('{exam_id}_complete.json', 'r', encoding='utf-8') as f:
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
    
    with open('{exam_id}_complete.json', 'w', encoding='utf-8') as f:
        json.dump(exam, f, ensure_ascii=False, indent=2)
    
    print(f"\\n✅ Updated {{updated}} answers in {exam_id}_complete.json")

if __name__ == "__main__":
    print("="*60)
    print("{exam_id} Answer Parser")
    print("="*60)
    print()
    print("⚠️  Instructions:")
    print("1. Go to: https://mandarinbean.com/{exam_id.lower()}-listening/")
    print("2. Click 'View Result' button")
    print("3. Save page as: {exam_id} Listening - Mandarin Bean.html")
    print()
    print("4. Go to: https://mandarinbean.com/{exam_id.lower()}-reading/")
    print("5. Click 'View Result' button")
    print("6. Save page as: {exam_id} Reading - Mandarin Bean.html")
    print()
    print("7. Run this script again")
    print("="*60)
    
    import os
    listening_file = "{exam_id} Listening - Mandarin Bean.html"
    reading_file = "{exam_id} Reading - Mandarin Bean.html"
    
    if os.path.exists(listening_file) and os.path.exists(reading_file):
        print("\\n✅ Found HTML files, parsing...\\n")
        
        listening_ans = parse_{exam_id.lower()}_answers(listening_file, 'listening')
        print(f"\\nListening: {{len(listening_ans)}} answers")
        
        reading_ans = parse_{exam_id.lower()}_answers(reading_file, 'reading')
        print(f"Reading: {{len(reading_ans)}} answers")
        
        update_json(listening_ans, reading_ans)
        
        print("\\n🎉 Done! Check {exam_id}_complete.json")
    else:
        print("\\n⚠️  HTML files not found. Please follow instructions above.")
'''
    
    parser_file = f"parse_{exam_id.lower()}_answers.py"
    with open(parser_file, 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print(f"✅ Created {parser_file}")
    return parser_file

if __name__ == "__main__":
    print("="*60)
    print("Creating HSK 2 Exam Templates: H20902 and H21003")
    print("="*60)
    print()
    
    exams = ["H20902", "H21003"]
    
    for exam_id in exams:
        print(f"\\n📝 Creating {exam_id}...")
        create_hsk2_exam_template(exam_id)
        create_html_parser_for_exam(exam_id)
        print(f"✅ {exam_id} template ready!")
    
    print("\\n" + "="*60)
    print("🎉 All templates created!")
    print("="*60)
    print("\\n📋 Next Steps:")
    print("\\n1. For H20902:")
    print("   - Visit: https://mandarinbean.com/h20902-listening/")
    print("   - Click 'View Result', save HTML")
    print("   - Visit: https://mandarinbean.com/h20902-reading/")
    print("   - Click 'View Result', save HTML")
    print("   - Run: python parse_h20902_answers.py")
    print("\\n2. For H21003:")
    print("   - Visit: https://mandarinbean.com/h21003-listening/")
    print("   - Click 'View Result', save HTML")
    print("   - Visit: https://mandarinbean.com/h21003-reading/")
    print("   - Click 'View Result', save HTML")
    print("   - Run: python parse_h21003_answers.py")
    print("\\n3. Verify:")
    print("   - python verify_h20902.py")
    print("   - python verify_h21003.py")
