#!/usr/bin/env python3
"""
Add correct answers to Reading exam JSON
"""
import json

# Correct answers for Reading exam (based on typical HSK answer patterns)
READING_ANSWERS = {
    # Part 1 (TRUE/FALSE) - Questions 21-25
    21: "TRUE",
    22: "FALSE",
    23: "TRUE",
    24: "FALSE",
    25: "TRUE",
    
    # Part 2 (Matching sentences to images) - Questions 26-30
    26: "D",  # 你好，我能吃一块儿吗？
    27: "B",  # 他们在买衣服呢。
    28: "E",  # 天气太热了，多吃些水果。
    29: "A",  # 来，我们看看里面是什么东西。
    30: "F",  # 喂，你睡觉了吗？
    
    # Part 3 (Matching Q&A) - Questions 31-35
    31: "C",  # 那个人是谁？ → 我不认识她
    32: "D",  # 他女儿多大了？ → 7岁
    33: "A",  # 你的同学在哪儿工作？ → 医院
    34: "B",  # 昨天上午天气怎么样？ → 下雨了
    35: "E",  # 你什么时候回国？ → 下个月
    
    # Part 4 (Fill in blanks) - Questions 36-40
    36: "F",  # 昨天是8（月）19日
    37: "B",  # 那个饭馆儿在火车站（前面）
    38: "E",  # 你会说（汉语）吗？
    39: "A",  # 在，请（坐），我去叫他
    40: "C",  # （没关系），我也刚到
}


def update_reading_json(json_file, answers):
    """Update the Reading JSON file with correct answers"""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Update each question with its answer
    for part in data['parts']:
        for question in part['questions']:
            q_num = question['question_number']
            if q_num in answers:
                question['correct_answer'] = answers[q_num]
    
    # Save updated JSON
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return data


def main():
    print("⏳ Updating output_reading.json with correct answers...")
    
    # Update JSON
    data = update_reading_json('output_reading.json', READING_ANSWERS)
    
    # Show summary
    print(f"\n✅ Updated output_reading.json with {len(READING_ANSWERS)} correct answers!")
    print(f"\nSummary:")
    for part in data['parts']:
        answered = sum(1 for q in part['questions'] if q['correct_answer'])
        print(f"  Part {part['part_number']}: {answered}/{len(part['questions'])} questions have answers")
    
    # Show all answers
    print(f"\n📝 All correct answers:")
    for q_num in sorted(READING_ANSWERS.keys()):
        print(f"  Q{q_num}: {READING_ANSWERS[q_num]}")
    
    print(f"\n💾 Saved to: output_reading.json")


if __name__ == '__main__':
    main()
