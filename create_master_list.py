#!/usr/bin/env python3
"""
Create a master file containing all HSK Level 1 exams
"""
import json
import os

def create_master_exam_list():
    """Load all exam files and create a master list"""
    
    exam_files = [
        "H10901_complete.json",
        "H10902_complete.json",
        "H11003_complete.json"
    ]
    
    exams = []
    
    for exam_file in exam_files:
        if os.path.exists(exam_file):
            with open(exam_file, 'r', encoding='utf-8') as f:
                exam_data = json.load(f)
                exams.append(exam_data)
            print(f"✅ Loaded {exam_file}")
        else:
            print(f"⚠️  {exam_file} not found")
    
    master_data = {
        "hsk_level": 1,
        "total_exams": len(exams),
        "total_questions": len(exams) * 40,
        "exams": exams,
        "metadata": {
            "created": "2025-10-29",
            "source": "mandarinbean.com",
            "description": "Complete HSK Level 1 exam collection",
            "exam_ids": [exam["exam_id"] for exam in exams]
        }
    }
    
    # Save master file
    with open('HSK1_all_exams.json', 'w', encoding='utf-8') as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)
    
    return master_data


def main():
    print("⏳ Creating master exam list...")
    
    master = create_master_exam_list()
    
    print(f"\n🎉 Master file created!")
    print(f"📊 HSK Level: {master['hsk_level']}")
    print(f"📝 Total Exams: {master['total_exams']}")
    print(f"❓ Total Questions: {master['total_questions']}")
    print(f"\n📋 Exams included:")
    for exam in master['exams']:
        print(f"  - {exam['exam_id']}: {exam['total_questions']} questions")
    
    print(f"\n💾 Saved to: HSK1_all_exams.json")
    
    # Print file sizes
    print(f"\n📦 File sizes:")
    for filename in ["H10901_complete.json", "H10902_complete.json", "H11003_complete.json", "HSK1_all_exams.json"]:
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            print(f"  {filename}: {size:,} bytes ({size/1024:.1f} KB)")


if __name__ == '__main__':
    main()
