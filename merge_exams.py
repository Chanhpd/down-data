#!/usr/bin/env python3
"""
Merge Listening and Reading exams into one complete HSK exam object
"""
import json

def merge_exams(listening_file, reading_file, output_file):
    """Merge listening and reading JSON files into one complete exam"""
    
    # Load both files
    with open(listening_file, 'r', encoding='utf-8') as f:
        listening = json.load(f)
    
    with open(reading_file, 'r', encoding='utf-8') as f:
        reading = json.load(f)
    
    # Create merged exam object
    merged_exam = {
        "exam_id": "H10901",
        "exam_title": "HSK Level 1 - H10901 Complete Exam",
        "exam_level": 1,
        "total_questions": 40,
        "total_time_minutes": 32,  # 15 listening + 17 reading
        "sections": [
            {
                "section_type": "listening",
                "section_title": "听力 (Listening)",
                "exam_url": listening["exam_url"],
                "audio_file": listening["audio_file"],
                "time_limit_minutes": 15,
                "question_range": "Q1-Q20",
                "total_parts": listening["total_parts"],
                "total_questions": listening["total_questions"],
                "parts": listening["parts"]
            },
            {
                "section_type": "reading",
                "section_title": "阅读 (Reading)",
                "exam_url": reading["exam_url"],
                "audio_file": None,
                "time_limit_minutes": reading["time_limit_minutes"],
                "question_range": "Q21-Q40",
                "total_parts": reading["total_parts"],
                "total_questions": reading["total_questions"],
                "parts": reading["parts"]
            }
        ],
        "metadata": {
            "created": "2025-10-29",
            "source": "mandarinbean.com",
            "hsk_level": 1,
            "total_listening_questions": 20,
            "total_reading_questions": 20,
            "has_audio": True,
            "has_images": True
        }
    }
    
    # Save merged file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_exam, f, ensure_ascii=False, indent=2)
    
    return merged_exam


def main():
    print("⏳ Merging Listening and Reading exams...")
    
    exam = merge_exams('output.json', 'output_reading.json', 'H10901_complete.json')
    
    print(f"\n✅ Successfully merged exams!")
    print(f"📊 Exam ID: {exam['exam_id']}")
    print(f"📝 Total Questions: {exam['total_questions']}")
    print(f"⏱️  Total Time: {exam['total_time_minutes']} minutes")
    print(f"\n📑 Sections:")
    for section in exam['sections']:
        print(f"  - {section['section_title']}: {section['question_range']} ({section['total_questions']} questions)")
    
    print(f"\n💾 Saved to: H10901_complete.json")


if __name__ == '__main__':
    main()
