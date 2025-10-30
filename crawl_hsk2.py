#!/usr/bin/env python3
"""
Crawl HSK Level 2 exams
Structure: 35 questions for Listening, different from HSK 1
"""
import json

def create_hsk2_listening(exam_id: str) -> dict:
    """
    Create HSK 2 Listening structure
    HSK 2 Listening: 35 questions, 4 parts, ~25 minutes
    """
    
    # Extract exam number (H20901 -> H2_09_01)
    exam_number = exam_id.replace("H", "H").replace("0", "_0", 1).replace("1", "_1", 1)
    
    exam_data = {
        "exam_url": f"https://mandarinbean.com/{exam_id.lower()}-listening/",
        "exam_title": f"{exam_id} Listening",
        "audio_file": f"https://traffic.libsyn.com/secure/learnchinese/{exam_id}.mp3",
        "total_parts": 4,
        "total_questions": 35,
        "parts": [
            {
                "part_number": 1,
                "part_title": "第一部分",
                "description": "第 1-10 题",
                "question_type": "TRUE_FALSE",
                "instructions": "判断对错",
                "questions": [
                    {
                        "question_number": i,
                        "question_text": f"Question {i}",
                        "image": None,
                        "options": [
                            {"option": "TRUE", "text": "TRUE"},
                            {"option": "FALSE", "text": "FALSE"}
                        ],
                        "correct_answer": None
                    } for i in range(1, 11)
                ]
            },
            {
                "part_number": 2,
                "part_title": "第二部分",
                "description": "第 11-25 题 (2 sub-parts)",
                "question_type": "MULTIPLE_CHOICE_DIALOGUE",
                "instructions": "听对话选择",
                "sub_parts": [
                    {
                        "sub_part": "11-15",
                        "description": "第 11-15 题",
                        "questions": [
                            {
                                "question_number": i,
                                "question_text": f"Question {i}",
                                "dialogue": None,
                                "image": None,
                                "options": [
                                    {"option": "A", "text": "A"},
                                    {"option": "B", "text": "B"},
                                    {"option": "C", "text": "C"},
                                    {"option": "D", "text": "D"},
                                    {"option": "E", "text": "E"},
                                    {"option": "F", "text": "F"}
                                ],
                                "correct_answer": None
                            } for i in range(11, 16)
                        ]
                    },
                    {
                        "sub_part": "16-20",
                        "description": "第 16-20 题",
                        "questions": [
                            {
                                "question_number": i,
                                "question_text": f"Question {i}",
                                "dialogue": None,
                                "image": None,
                                "options": [
                                    {"option": "A", "text": "A"},
                                    {"option": "B", "text": "B"},
                                    {"option": "C", "text": "C"},
                                    {"option": "D", "text": "D"},
                                    {"option": "E", "text": "E"},
                                    {"option": "F", "text": "F"}
                                ],
                                "correct_answer": None
                            } for i in range(16, 21)
                        ]
                    }
                ],
                "questions": []  # Empty, use sub_parts instead
            },
            {
                "part_number": 3,
                "part_title": "第三部分",
                "description": "第 21-30 题",
                "question_type": "MULTIPLE_CHOICE_TEXT",
                "instructions": "听短文选择正确答案",
                "questions": [
                    {
                        "question_number": i,
                        "question_text": f"Question {i}",
                        "passage": None,
                        "image": None,
                        "options": [
                            {"option": "A", "text": "Option A"},
                            {"option": "B", "text": "Option B"},
                            {"option": "C", "text": "Option C"}
                        ],
                        "correct_answer": None
                    } for i in range(21, 31)
                ]
            },
            {
                "part_number": 4,
                "part_title": "第四部分",
                "description": "第 31-35 题",
                "question_type": "COMPREHENSION",
                "instructions": "听对话或短文回答问题",
                "questions": [
                    {
                        "question_number": i,
                        "question_text": f"Question {i}",
                        "passage": None,
                        "question": None,
                        "image": None,
                        "options": [
                            {"option": "A", "text": "Option A"},
                            {"option": "B", "text": "Option B"},
                            {"option": "C", "text": "Option C"}
                        ],
                        "correct_answer": None
                    } for i in range(31, 36)
                ]
            }
        ]
    }
    
    return exam_data


def create_hsk2_reading(exam_id: str) -> dict:
    """
    Create HSK 2 Reading structure
    HSK 2 Reading: 25 questions, 4 parts, ~22 minutes
    """
    
    exam_data = {
        "exam_url": f"https://mandarinbean.com/{exam_id.lower()}-reading/",
        "exam_title": f"{exam_id} Reading",
        "exam_type": "reading",
        "time_limit_minutes": 22,
        "total_parts": 4,
        "total_questions": 25,
        "parts": [
            {
                "part_number": 1,
                "part_title": "第一部分",
                "description": "第 36-40 题",
                "question_type": "SENTENCE_PICTURE_MATCH",
                "instructions": "看图选择正确的句子",
                "questions": [
                    {
                        "question_number": i,
                        "question_text": f"Question {i}",
                        "image": None,
                        "options": [
                            {"option": "A", "text": "Sentence A"},
                            {"option": "B", "text": "Sentence B"}
                        ],
                        "correct_answer": None
                    } for i in range(36, 41)
                ]
            },
            {
                "part_number": 2,
                "part_title": "第二部分",
                "description": "第 41-45 题",
                "question_type": "SENTENCE_COMPLETION",
                "instructions": "选词填空",
                "questions": [
                    {
                        "question_number": i,
                        "question_text": f"Question {i}",
                        "sentence": None,
                        "options": [
                            {"option": "A", "text": "Word A"},
                            {"option": "B", "text": "Word B"},
                            {"option": "C", "text": "Word C"}
                        ],
                        "correct_answer": None
                    } for i in range(41, 46)
                ]
            },
            {
                "part_number": 3,
                "part_title": "第三部分",
                "description": "第 46-50 题",
                "question_type": "DIALOGUE_COMPLETION",
                "instructions": "选择合适的句子完成对话",
                "questions": [
                    {
                        "question_number": i,
                        "question_text": f"Question {i}",
                        "dialogue": None,
                        "options": [
                            {"option": "A", "text": "Response A"},
                            {"option": "B", "text": "Response B"},
                            {"option": "C", "text": "Response C"}
                        ],
                        "correct_answer": None
                    } for i in range(46, 51)
                ]
            },
            {
                "part_number": 4,
                "part_title": "第四部分",
                "description": "第 51-60 题",
                "question_type": "READING_COMPREHENSION",
                "instructions": "阅读短文回答问题",
                "questions": [
                    {
                        "question_number": i,
                        "question_text": f"Question {i}",
                        "passage": None,
                        "question": None,
                        "options": [
                            {"option": "A", "text": "Answer A"},
                            {"option": "B", "text": "Answer B"},
                            {"option": "C", "text": "Answer C"}
                        ],
                        "correct_answer": None
                    } for i in range(51, 61)
                ]
            }
        ]
    }
    
    return exam_data


def create_hsk2_complete_exam(exam_id: str) -> dict:
    """Create a complete HSK 2 exam with listening and reading"""
    
    listening = create_hsk2_listening(exam_id)
    reading = create_hsk2_reading(exam_id)
    
    complete_exam = {
        "exam_id": exam_id,
        "exam_title": f"HSK Level 2 - {exam_id} Complete Exam",
        "exam_level": 2,
        "total_questions": 60,  # 35 listening + 25 reading
        "total_time_minutes": 47,  # 25 listening + 22 reading
        "sections": [
            {
                "section_type": "listening",
                "section_title": "听力 (Listening)",
                "exam_url": listening["exam_url"],
                "audio_file": listening["audio_file"],
                "time_limit_minutes": 25,
                "question_range": "Q1-Q35",
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
                "question_range": "Q36-Q60",
                "total_parts": reading["total_parts"],
                "total_questions": reading["total_questions"],
                "parts": reading["parts"]
            }
        ],
        "metadata": {
            "created": "2025-10-29",
            "source": "mandarinbean.com",
            "hsk_level": 2,
            "total_listening_questions": 35,
            "total_reading_questions": 25,
            "has_audio": True,
            "has_images": True,
            "note": "HSK 2 has different structure: 35 listening + 25 reading = 60 total"
        }
    }
    
    return complete_exam


def main():
    exam_ids = ["H20901"]
    
    for exam_id in exam_ids:
        print(f"\n⏳ Creating HSK 2 exam {exam_id}...")
        
        exam = create_hsk2_complete_exam(exam_id)
        
        filename = f"{exam_id}_complete.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(exam, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Created {filename}")
        print(f"   📊 Level: HSK {exam['exam_level']}")
        print(f"   📝 Total: {exam['total_questions']} questions")
        print(f"   🎧 Listening: {exam['sections'][0]['total_questions']} questions")
        print(f"   📖 Reading: {exam['sections'][1]['total_questions']} questions")
        print(f"   ⏱️  Time: {exam['total_time_minutes']} minutes")
    
    print(f"\n🎉 HSK 2 exam created!")
    print(f"\n📋 Structure difference:")
    print(f"   HSK 1: 20 listening + 20 reading = 40 questions")
    print(f"   HSK 2: 35 listening + 25 reading = 60 questions ⭐")


if __name__ == '__main__':
    main()
