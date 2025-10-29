#!/usr/bin/env python3
"""
crawl_hsk_manual.py

Manual HSK exam data extractor based on observed structure.
Since the page uses heavy JavaScript, this version requires manual content extraction.

For now, this creates a properly structured JSON template that matches the API requirements.
"""
import json

# Based on the actual content from https://mandarinbean.com/h10901-listening/
# This data was extracted from the fetch_webpage tool output

exam_data = {
    "exam_url": "https://mandarinbean.com/h10901-listening/",
    "exam_title": "H10901 Listening",
    "audio_file": "https://traffic.libsyn.com/secure/learnchinese/H10901.mp3",
    "total_parts": 4,
    "total_questions": 20,
    "parts": [
        {
            "part_number": 1,
            "part_title": "第一部分",
            "description": "第 1-5 题",
            "question_type": "TRUE_FALSE",
            "questions": [
                {
                    "question_number": 1,
                    "question_text": "Question 1",
                    "image": "https://mandarinbean.com/wp-content/uploads/2020/12/H1_1.png",
                    "options": [
                        {"option": "TRUE", "text": "TRUE"},
                        {"option": "FALSE", "text": "FALSE"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 2,
                    "question_text": "Question 2",
                    "image": "https://mandarinbean.com/wp-content/uploads/2020/12/H1_2.png",
                    "options": [
                        {"option": "TRUE", "text": "TRUE"},
                        {"option": "FALSE", "text": "FALSE"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 3,
                    "question_text": "Question 3",
                    "image": "https://mandarinbean.com/wp-content/uploads/2020/12/H1_3.png",
                    "options": [
                        {"option": "TRUE", "text": "TRUE"},
                        {"option": "FALSE", "text": "FALSE"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 4,
                    "question_text": "Question 4",
                    "image": "https://mandarinbean.com/wp-content/uploads/2020/12/H1_4.png",
                    "options": [
                        {"option": "TRUE", "text": "TRUE"},
                        {"option": "FALSE", "text": "FALSE"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 5,
                    "question_text": "Question 5",
                    "image": "https://mandarinbean.com/wp-content/uploads/2020/12/H1_5.png",
                    "options": [
                        {"option": "TRUE", "text": "TRUE"},
                        {"option": "FALSE", "text": "FALSE"}
                    ],
                    "correct_answer": None
                }
            ]
        },
        {
            "part_number": 2,
            "part_title": "第二部分",
            "description": "第 6-10 题",
            "question_type": "MULTIPLE_CHOICE",
            "questions": [
                {
                    "question_number": 6,
                    "question_text": "Question 6",
                    "image": "https://mandarinbean.com/wp-content/uploads/2020/12/H1_6.png",
                    "options": [
                        {"option": "A", "text": "A"},
                        {"option": "B", "text": "B"},
                        {"option": "C", "text": "C"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 7,
                    "question_text": "Question 7",
                    "image": "https://mandarinbean.com/wp-content/uploads/2020/12/H1_7-1.jpg",
                    "options": [
                        {"option": "A", "text": "A"},
                        {"option": "B", "text": "B"},
                        {"option": "C", "text": "C"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 8,
                    "question_text": "Question 8",
                    "image": "https://mandarinbean.com/wp-content/uploads/2020/12/H1_8.jpg",
                    "options": [
                        {"option": "A", "text": "A"},
                        {"option": "B", "text": "B"},
                        {"option": "C", "text": "C"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 9,
                    "question_text": "Question 9",
                    "image": "https://mandarinbean.com/wp-content/uploads/2020/12/H1_9.jpg",
                    "options": [
                        {"option": "A", "text": "A"},
                        {"option": "B", "text": "B"},
                        {"option": "C", "text": "C"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 10,
                    "question_text": "Question 10",
                    "image": "https://mandarinbean.com/wp-content/uploads/2020/12/H1_10.jpg",
                    "options": [
                        {"option": "A", "text": "A"},
                        {"option": "B", "text": "B"},
                        {"option": "C", "text": "C"}
                    ],
                    "correct_answer": None
                }
            ]
        },
        {
            "part_number": 3,
            "part_title": "第三部分",
            "description": "第 11-15 题",
            "question_type": "MATCHING",
            "questions": [
                {
                    "question_number": 11,
                    "question_text": "Question 11",
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
                },
                {
                    "question_number": 12,
                    "question_text": "Question 12",
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
                },
                {
                    "question_number": 13,
                    "question_text": "Question 13",
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
                },
                {
                    "question_number": 14,
                    "question_text": "Question 14",
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
                },
                {
                    "question_number": 15,
                    "question_text": "Question 15",
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
                }
            ]
        },
        {
            "part_number": 4,
            "part_title": "第四部分",
            "description": "第 16-20 题",
            "question_type": "MULTIPLE_CHOICE_TEXT",
            "questions": [
                {
                    "question_number": 16,
                    "question_text": "Question 16",
                    "image": None,
                    "options": [
                        {"option": "A", "text": "他的 (tā de)"},
                        {"option": "B", "text": "我的 (wǒ de)"},
                        {"option": "C", "text": "同学的 (tóngxué de)"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 17,
                    "question_text": "Question 17",
                    "image": None,
                    "options": [
                        {"option": "A", "text": "星期三 (xīngqīsān)"},
                        {"option": "B", "text": "星期五 (xīngqīwǔ)"},
                        {"option": "C", "text": "星期六 (xīngqīliù)"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 18,
                    "question_text": "Question 18",
                    "image": None,
                    "options": [
                        {"option": "A", "text": "5"},
                        {"option": "B", "text": "15"},
                        {"option": "C", "text": "50"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 19,
                    "question_text": "Question 19",
                    "image": None,
                    "options": [
                        {"option": "A", "text": "茶 (chá)"},
                        {"option": "B", "text": "苹果 (píngguǒ)"},
                        {"option": "C", "text": "杯子 (bēizi)"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 20,
                    "question_text": "Question 20",
                    "image": None,
                    "options": [
                        {"option": "A", "text": "爱学习 (ài xuéxí)"},
                        {"option": "B", "text": "很漂亮 (hěn piàoliang)"},
                        {"option": "C", "text": "想回家 (xiǎng huí jiā)"}
                    ],
                    "correct_answer": None
                }
            ]
        }
    ],
    "metadata": {
        "note": "This is a structured template based on HSK H10901 Listening exam",
        "images_total": 10,
        "requires_audio": True
    }
}

# Save to JSON
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print("✅ Created structured exam data!")
print(f"📊 {exam_data['total_parts']} parts, {exam_data['total_questions']} questions")
print(f"🎵 Audio: {exam_data['audio_file']}")
print(f"💾 Saved to: output.json")
print("\nStructure ready for API consumption!")
