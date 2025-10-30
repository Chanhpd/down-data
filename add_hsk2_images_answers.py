import json

def add_images_and_answers_hsk2():
    """Add image URLs and correct_answer field to HSK 2 exam"""
    
    with open('H20901_complete.json', 'r', encoding='utf-8') as f:
        exam = json.load(f)
    
    # Image URL base pattern for HSK 2
    # Actual pattern from website: https://mandarinbean.com/wp-content/uploads/2020/12/h2_{question_num}.jpg
    base_url = "https://mandarinbean.com/wp-content/uploads/2020/12/"
    
    # Listening Section Images
    listening = exam['sections'][0]
    
    # Part 1 (Q1-Q10): TRUE/FALSE - HAS IMAGES!
    part1 = listening['parts'][0]
    for question in part1['questions']:
        q_num = question['question_number']
        question['image_url'] = f"{base_url}h2_{q_num}.jpg"
        question['correct_answer'] = ""  # To be filled manually
    
    # Part 2 (Q11-Q20): Multiple choice dialogues with images
    part2 = listening['parts'][1]
    
    # Part 2 has sub-parts, need to iterate through them
    if 'sub_parts' in part2:
        for sub_part in part2['sub_parts']:
            for question in sub_part['questions']:
                q_num = question['question_number']
                if q_num >= 11 and q_num <= 20:  # Fixed: Part 2 is Q11-Q20, not Q25
                    question['image_url'] = f"{base_url}h2_{q_num}.jpg"
                    question['correct_answer'] = ""  # To be filled manually
    else:
        # Fallback if no sub_parts
        for question in part2.get('questions', []):
            q_num = question['question_number']
            if q_num >= 11 and q_num <= 20:
                question['image_url'] = f"{base_url}h2_{q_num}.jpg"
                question['correct_answer'] = ""  # To be filled manually
    
    # Part 3 (Q21-Q30): Multiple choice with text - ALSO HAS IMAGES!
    part3 = listening['parts'][2]
    for question in part3['questions']:
        q_num = question['question_number']
        question['image_url'] = f"{base_url}h2_{q_num}.jpg"
        question['correct_answer'] = ""  # To be filled manually
    
    # Part 4 (Q31-Q35): Comprehension - ALSO HAS IMAGES!
    part4 = listening['parts'][3]
    for question in part4['questions']:
        q_num = question['question_number']
        question['image_url'] = f"{base_url}h2_{q_num}.jpg"
        question['correct_answer'] = ""  # To be filled manually
    
    # Reading Section Images
    reading = exam['sections'][1]
    
    # Part 1 (Q36-Q40): Sentence-Picture Match - HAS IMAGES
    part1_reading = reading['parts'][0]
    for question in part1_reading['questions']:
        q_num = question['question_number']
        question['image_url'] = f"{base_url}h2_{q_num}.jpg"
        question['correct_answer'] = ""  # To be filled manually
    
    # Part 2 (Q41-Q45): Fill in blank - no images
    part2_reading = reading['parts'][1]
    for question in part2_reading['questions']:
        question['correct_answer'] = ""  # To be filled manually
    
    # Part 3 (Q46-Q50): TRUE/FALSE - no images
    part3_reading = reading['parts'][2]
    for question in part3_reading['questions']:
        question['correct_answer'] = ""  # To be filled manually
    
    # Part 4 (Q51-Q60): Reading comprehension - no images usually
    part4_reading = reading['parts'][3]
    for question in part4_reading['questions']:
        question['correct_answer'] = ""  # To be filled manually
    
    # Save updated file
    with open('H20901_complete.json', 'w', encoding='utf-8') as f:
        json.dump(exam, f, ensure_ascii=False, indent=2)
    
    print("✅ Updated H20901_complete.json with:")
    print("   - Image URLs for ALL Listening questions (Q1-Q35)")
    print("   - Image URLs for Reading Part 1 (Q36-Q40)")
    print("   - correct_answer field added to all 60 questions")
    print(f"\n📸 Total images: 40 (35 listening + 5 reading)")
    print("   Pattern: https://mandarinbean.com/wp-content/uploads/2020/12/h2_{{number}}.jpg")
    print("\n⚠️  Note: correct_answer fields are empty - need to fill manually")
    print("   You can add answers from the website or answer key")

if __name__ == "__main__":
    add_images_and_answers_hsk2()
