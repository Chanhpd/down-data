import json

def verify_h21003_complete():
    """Verify H21003 complete exam has all answers and images"""
    
    with open('H21003_complete.json', 'r', encoding='utf-8') as f:
        exam = json.load(f)
    
    print("="*70)
    print(f"📋 {exam['exam_title']}")
    print("="*70)
    print(f"Level: HSK {exam['exam_level']}")
    print(f"Total Questions: {exam['total_questions']}")
    print(f"Total Time: {exam['total_time_minutes']} minutes")
    print()
    
    total_with_answers = 0
    total_with_images = 0
    total_questions = 0
    
    for section in exam['sections']:
        print(f"\n{'='*70}")
        print(f"📚 {section['section_title']}")
        print(f"   Questions: {section['question_range']}")
        print(f"   Time: {section['time_limit_minutes']} minutes")
        print(f"   Audio: {section.get('audio_file', 'N/A')}")
        print("="*70)
        
        for part in section['parts']:
            part_num = part['part_number']
            part_title = part['part_title']
            q_type = part['question_type']
            
            # Handle sub_parts
            if 'sub_parts' in part and part['sub_parts']:
                print(f"\n  Part {part_num}: {part_title} ({q_type})")
                for sub_part in part['sub_parts']:
                    questions = sub_part['questions']
                    with_ans = sum(1 for q in questions if q.get('correct_answer'))
                    with_img = sum(1 for q in questions if q.get('image_url'))
                    total_questions += len(questions)
                    total_with_answers += with_ans
                    total_with_images += with_img
                    
                    q_range = f"Q{questions[0]['question_number']}-Q{questions[-1]['question_number']}"
                    print(f"    {sub_part['description']}: {len(questions)} questions")
                    print(f"      Range: {q_range}")
                    print(f"      ✅ Answers: {with_ans}/{len(questions)}")
                    print(f"      🖼️  Images: {with_img}/{len(questions)}")
            else:
                questions = part.get('questions', [])
                if questions:
                    with_ans = sum(1 for q in questions if q.get('correct_answer'))
                    with_img = sum(1 for q in questions if q.get('image_url'))
                    total_questions += len(questions)
                    total_with_answers += with_ans
                    total_with_images += with_img
                    
                    q_range = f"Q{questions[0]['question_number']}-Q{questions[-1]['question_number']}"
                    print(f"\n  Part {part_num}: {part_title} ({q_type})")
                    print(f"    Range: {q_range}, {len(questions)} questions")
                    print(f"    ✅ Answers: {with_ans}/{len(questions)}")
                    print(f"    🖼️  Images: {with_img}/{len(questions)}")
    
    print("\n" + "="*70)
    print("📊 SUMMARY")
    print("="*70)
    print(f"Total Questions: {total_questions}")
    print(f"✅ Questions with Answers: {total_with_answers}/{total_questions} ({total_with_answers/total_questions*100:.1f}%)")
    print(f"🖼️  Questions with Images: {total_with_images}/{total_questions} ({total_with_images/total_questions*100:.1f}%)")
    
    if total_with_answers == total_questions:
        print("\n🎉 ALL QUESTIONS HAVE ANSWERS! ✅")
    else:
        print(f"\n⚠️  Missing {total_questions - total_with_answers} answers")
    
    print("="*70)

if __name__ == "__main__":
    verify_h21003_complete()
