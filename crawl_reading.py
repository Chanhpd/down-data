#!/usr/bin/env python3
"""
crawl_reading.py

Crawl HSK Reading exam with structured data for API.
"""
import json

# Based on the content from https://mandarinbean.com/h10901-reading/
exam_data = {
    "exam_url": "https://mandarinbean.com/h10901-reading/",
    "exam_title": "H10901 Reading",
    "exam_type": "reading",
    "time_limit_minutes": 17,
    "total_parts": 4,
    "total_questions": 20,
    "parts": [
        {
            "part_number": 1,
            "part_title": "第一部分",
            "description": "第 21-25 题",
            "question_type": "TRUE_FALSE",
            "instructions": "判断对错",
            "questions": [
                {
                    "question_number": 21,
                    "question_text": "Question 21",
                    "passage": None,
                    "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_1.png",
                    "options": [
                        {"option": "TRUE", "text": "TRUE"},
                        {"option": "FALSE", "text": "FALSE"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 22,
                    "question_text": "Question 22",
                    "passage": None,
                    "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_2.png",
                    "options": [
                        {"option": "TRUE", "text": "TRUE"},
                        {"option": "FALSE", "text": "FALSE"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 23,
                    "question_text": "Question 23",
                    "passage": None,
                    "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_3.png",
                    "options": [
                        {"option": "TRUE", "text": "TRUE"},
                        {"option": "FALSE", "text": "FALSE"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 24,
                    "question_text": "Question 24",
                    "passage": None,
                    "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_4.png",
                    "options": [
                        {"option": "TRUE", "text": "TRUE"},
                        {"option": "FALSE", "text": "FALSE"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 25,
                    "question_text": "Question 25",
                    "passage": None,
                    "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_5.png",
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
            "description": "第 26-30 题",
            "question_type": "MATCHING_SENTENCE",
            "instructions": "选词填空 - 为句子选择合适的图片",
            "questions": [
                {
                    "question_number": 26,
                    "question_text": "你好，我能吃一块儿吗？",
                    "question_text_pinyin": "Nǐ hǎo, wǒ néng chī yí kuàir ma?",
                    "passage": None,
                    "image": None,
                    "options": [
                        {"option": "A", "text": "A", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_6.png"},
                        {"option": "B", "text": "B", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_7.png"},
                        {"option": "C", "text": "C", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_8.png"},
                        {"option": "D", "text": "D", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_9.png"},
                        {"option": "E", "text": "E", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_10.png"},
                        {"option": "F", "text": "F", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_11.png"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 27,
                    "question_text": "他们在买衣服呢。",
                    "question_text_pinyin": "Tāmen zài mǎi yīfu ne.",
                    "passage": None,
                    "image": None,
                    "options": [
                        {"option": "A", "text": "A", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_6.png"},
                        {"option": "B", "text": "B", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_7.png"},
                        {"option": "C", "text": "C", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_8.png"},
                        {"option": "D", "text": "D", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_9.png"},
                        {"option": "E", "text": "E", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_10.png"},
                        {"option": "F", "text": "F", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_11.png"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 28,
                    "question_text": "天气太热了，多吃些水果。",
                    "question_text_pinyin": "Tiānqì tài rè le, duō chī xiē shuǐguǒ.",
                    "passage": None,
                    "image": None,
                    "options": [
                        {"option": "A", "text": "A", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_6.png"},
                        {"option": "B", "text": "B", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_7.png"},
                        {"option": "C", "text": "C", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_8.png"},
                        {"option": "D", "text": "D", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_9.png"},
                        {"option": "E", "text": "E", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_10.png"},
                        {"option": "F", "text": "F", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_11.png"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 29,
                    "question_text": "来，我们看看里面是什么东西。",
                    "question_text_pinyin": "Lái, wǒmen kànkan lǐmiàn shì shénme dōngxi.",
                    "passage": None,
                    "image": None,
                    "options": [
                        {"option": "A", "text": "A", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_6.png"},
                        {"option": "B", "text": "B", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_7.png"},
                        {"option": "C", "text": "C", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_8.png"},
                        {"option": "D", "text": "D", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_9.png"},
                        {"option": "E", "text": "E", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_10.png"},
                        {"option": "F", "text": "F", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_11.png"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 30,
                    "question_text": "喂，你睡觉了吗？",
                    "question_text_pinyin": "Wéi, nǐ shuìjiào le ma?",
                    "passage": None,
                    "image": None,
                    "options": [
                        {"option": "A", "text": "A", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_6.png"},
                        {"option": "B", "text": "B", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_7.png"},
                        {"option": "C", "text": "C", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_8.png"},
                        {"option": "D", "text": "D", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_9.png"},
                        {"option": "E", "text": "E", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_10.png"},
                        {"option": "F", "text": "F", "image": "https://mandarinbean.com/wp-content/uploads/2020/12/R1_11.png"}
                    ],
                    "correct_answer": None
                }
            ]
        },
        {
            "part_number": 3,
            "part_title": "第三部分",
            "description": "第 31-35 题",
            "question_type": "MATCHING_QUESTION_ANSWER",
            "instructions": "为问题选择正确的回答",
            "shared_options": [
                {"option": "A", "text": "医院 (Yīyuàn)"},
                {"option": "B", "text": "下雨了 (Xià yǔ le)"},
                {"option": "C", "text": "我不认识她 (Wǒ bú rènshi tā)"},
                {"option": "D", "text": "7岁 (suì)"},
                {"option": "E", "text": "下个月 (Xià ge yuè)"},
                {"option": "F", "text": "好的，谢谢 (Hǎo de, xièxie)"}
            ],
            "questions": [
                {
                    "question_number": 31,
                    "question_text": "那个人是谁？",
                    "question_text_pinyin": "Nàge rén shì shéi?",
                    "passage": None,
                    "image": None,
                    "options": [
                        {"option": "A", "text": "医院 (Yīyuàn)"},
                        {"option": "B", "text": "下雨了 (Xià yǔ le)"},
                        {"option": "C", "text": "我不认识她 (Wǒ bú rènshi tā)"},
                        {"option": "D", "text": "7岁 (suì)"},
                        {"option": "E", "text": "下个月 (Xià ge yuè)"},
                        {"option": "F", "text": "好的，谢谢 (Hǎo de, xièxie)"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 32,
                    "question_text": "他女儿多大了？",
                    "question_text_pinyin": "Tā nǚ'ér duō dà le?",
                    "passage": None,
                    "image": None,
                    "options": [
                        {"option": "A", "text": "医院 (Yīyuàn)"},
                        {"option": "B", "text": "下雨了 (Xià yǔ le)"},
                        {"option": "C", "text": "我不认识她 (Wǒ bú rènshi tā)"},
                        {"option": "D", "text": "7岁 (suì)"},
                        {"option": "E", "text": "下个月 (Xià ge yuè)"},
                        {"option": "F", "text": "好的，谢谢 (Hǎo de, xièxie)"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 33,
                    "question_text": "你的同学在哪儿工作？",
                    "question_text_pinyin": "Nǐ de tóngxué zài nǎr gōngzuò?",
                    "passage": None,
                    "image": None,
                    "options": [
                        {"option": "A", "text": "医院 (Yīyuàn)"},
                        {"option": "B", "text": "下雨了 (Xià yǔ le)"},
                        {"option": "C", "text": "我不认识她 (Wǒ bú rènshi tā)"},
                        {"option": "D", "text": "7岁 (suì)"},
                        {"option": "E", "text": "下个月 (Xià ge yuè)"},
                        {"option": "F", "text": "好的，谢谢 (Hǎo de, xièxie)"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 34,
                    "question_text": "昨天上午天气怎么样？",
                    "question_text_pinyin": "Zuótiān shàngwǔ tiānqì zěnmeyàng?",
                    "passage": None,
                    "image": None,
                    "options": [
                        {"option": "A", "text": "医院 (Yīyuàn)"},
                        {"option": "B", "text": "下雨了 (Xià yǔ le)"},
                        {"option": "C", "text": "我不认识她 (Wǒ bú rènshi tā)"},
                        {"option": "D", "text": "7岁 (suì)"},
                        {"option": "E", "text": "下个月 (Xià ge yuè)"},
                        {"option": "F", "text": "好的，谢谢 (Hǎo de, xièxie)"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 35,
                    "question_text": "你什么时候回国？",
                    "question_text_pinyin": "Nǐ shénme shíhou huí guó?",
                    "passage": None,
                    "image": None,
                    "options": [
                        {"option": "A", "text": "医院 (Yīyuàn)"},
                        {"option": "B", "text": "下雨了 (Xià yǔ le)"},
                        {"option": "C", "text": "我不认识她 (Wǒ bú rènshi tā)"},
                        {"option": "D", "text": "7岁 (suì)"},
                        {"option": "E", "text": "下个月 (Xià ge yuè)"},
                        {"option": "F", "text": "好的，谢谢 (Hǎo de, xièxie)"}
                    ],
                    "correct_answer": None
                }
            ]
        },
        {
            "part_number": 4,
            "part_title": "第四部分",
            "description": "第 36-40 题",
            "question_type": "FILL_IN_BLANK",
            "instructions": "选词填空",
            "shared_options": [
                {"option": "A", "text": "坐 (zuò)"},
                {"option": "B", "text": "前面 (qiánmiàn)"},
                {"option": "C", "text": "没关系 (méi guānxi)"},
                {"option": "D", "text": "名字 (míngzi)"},
                {"option": "E", "text": "汉语 (Hànyǔ)"},
                {"option": "F", "text": "月 (yuè)"}
            ],
            "questions": [
                {
                    "question_number": 36,
                    "question_text": "昨天是8（ ）19日。",
                    "question_text_pinyin": "Zuótiān shì 8 ( ) 19 rì.",
                    "passage": None,
                    "image": None,
                    "options": [
                        {"option": "A", "text": "坐 (zuò)"},
                        {"option": "B", "text": "前面 (qiánmiàn)"},
                        {"option": "C", "text": "没关系 (méi guānxi)"},
                        {"option": "D", "text": "名字 (míngzi)"},
                        {"option": "E", "text": "汉语 (Hànyǔ)"},
                        {"option": "F", "text": "月 (yuè)"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 37,
                    "question_text": "那个饭馆儿在火车站（ ）。",
                    "question_text_pinyin": "Nàge fànguǎnr zài huǒchēzhàn ( ).",
                    "passage": None,
                    "image": None,
                    "options": [
                        {"option": "A", "text": "坐 (zuò)"},
                        {"option": "B", "text": "前面 (qiánmiàn)"},
                        {"option": "C", "text": "没关系 (méi guānxi)"},
                        {"option": "D", "text": "名字 (míngzi)"},
                        {"option": "E", "text": "汉语 (Hànyǔ)"},
                        {"option": "F", "text": "月 (yuè)"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 38,
                    "question_text": "你会说（ ）吗？",
                    "question_text_pinyin": "Nǐ huì shuō ( ) ma?",
                    "passage": None,
                    "image": None,
                    "options": [
                        {"option": "A", "text": "坐 (zuò)"},
                        {"option": "B", "text": "前面 (qiánmiàn)"},
                        {"option": "C", "text": "没关系 (méi guānxi)"},
                        {"option": "D", "text": "名字 (míngzi)"},
                        {"option": "E", "text": "汉语 (Hànyǔ)"},
                        {"option": "F", "text": "月 (yuè)"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 39,
                    "question_text": "男：你好，王先生在吗？\n女：在，请（ ），我去叫他。",
                    "question_text_pinyin": "Nán: Nǐ hǎo! Wáng xiānsheng zài ma?\nNǚ: Zài, qǐng ( ), wǒ qù jiào tā.",
                    "passage": None,
                    "image": None,
                    "options": [
                        {"option": "A", "text": "坐 (zuò)"},
                        {"option": "B", "text": "前面 (qiánmiàn)"},
                        {"option": "C", "text": "没关系 (méi guānxi)"},
                        {"option": "D", "text": "名字 (míngzi)"},
                        {"option": "E", "text": "汉语 (Hànyǔ)"},
                        {"option": "F", "text": "月 (yuè)"}
                    ],
                    "correct_answer": None
                },
                {
                    "question_number": 40,
                    "question_text": "男：对不起，我来晚了。\n女：（ ），我也刚到。",
                    "question_text_pinyin": "Nán: Duìbuqǐ, wǒ lái wǎn le.\nNǚ: ( ), wǒ yě gāng dào.",
                    "passage": None,
                    "image": None,
                    "options": [
                        {"option": "A", "text": "坐 (zuò)"},
                        {"option": "B", "text": "前面 (qiánmiàn)"},
                        {"option": "C", "text": "没关系 (méi guānxi)"},
                        {"option": "D", "text": "名字 (míngzi)"},
                        {"option": "E", "text": "汉语 (Hànyǔ)"},
                        {"option": "F", "text": "月 (yuè)"}
                    ],
                    "correct_answer": None
                }
            ]
        }
    ],
    "metadata": {
        "note": "HSK H10901 Reading exam structure",
        "has_audio": False,
        "has_images": True,
        "images_total": 11
    }
}

# Save to JSON
with open('output_reading.json', 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print("✅ Created structured Reading exam data!")
print(f"📊 {exam_data['total_parts']} parts, {exam_data['total_questions']} questions")
print(f"⏱️  Time limit: {exam_data['time_limit_minutes']} minutes")
print(f"🖼️  Images: {exam_data['metadata']['images_total']}")
print(f"💾 Saved to: output_reading.json")
print("\nStructure ready for API consumption!")
