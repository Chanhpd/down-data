import json

def fix_hsk1_images():
    """Fix image URLs for all HSK 1 exams with correct pattern"""
    
    # Correct base URL pattern
    base_url = "https://mandarinbean.com/wp-content/uploads/2020/12/"
    
    # Process all 3 HSK 1 exams
    exam_ids = ["H10901", "H10902", "H11003"]
    
    for exam_id in exam_ids:
        filename = f"{exam_id}_complete.json"
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                exam = json.load(f)
            
            print(f"\n📝 Processing {exam_id}...")
            
            # Listening Section
            listening = exam['sections'][0]
            
            # Part 2 (Q6-Q10): Has images
            part2 = listening['parts'][1]
            for question in part2['questions']:
                q_num = question['question_number']
                question['image_url'] = f"{base_url}h1_{q_num}.jpg"
                print(f"   ✅ L2 Q{q_num}: h1_{q_num}.jpg")
            
            # Part 3 (Q11-Q15): Has images (matching A-F)
            part3 = listening['parts'][2]
            for question in part3['questions']:
                q_num = question['question_number']
                question['image_url'] = f"{base_url}h1_{q_num}.jpg"
                print(f"   ✅ L3 Q{q_num}: h1_{q_num}.jpg")
            
            # Reading Section
            reading = exam['sections'][1]
            
            # Part 1 (Q21-Q25): Has images (TRUE/FALSE with pictures)
            part1_reading = reading['parts'][0]
            for question in part1_reading['questions']:
                q_num = question['question_number']
                question['image_url'] = f"{base_url}h1_{q_num}.jpg"
                print(f"   ✅ R1 Q{q_num}: h1_{q_num}.jpg")
            
            # Part 2 (Q26-Q30): Has images (matching)
            part2_reading = reading['parts'][1]
            for question in part2_reading['questions']:
                q_num = question['question_number']
                question['image_url'] = f"{base_url}h1_{q_num}.jpg"
                print(f"   ✅ R2 Q{q_num}: h1_{q_num}.jpg")
            
            # Save updated file
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(exam, f, ensure_ascii=False, indent=2)
            
            print(f"   💾 Saved {filename}")
            
        except FileNotFoundError:
            print(f"   ⚠️  File not found: {filename}")
            continue
    
    print("\n" + "="*60)
    print("✅ Updated HSK 1 image URLs with pattern:")
    print("   https://mandarinbean.com/wp-content/uploads/2020/12/h1_{number}.jpg")
    print("="*60)

if __name__ == "__main__":
    fix_hsk1_images()
