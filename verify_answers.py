import json

with open('output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=== Correct Answers Summary ===\n")

answer_map = {}
for part in data['parts']:
    for q in part['questions']:
        q_num = q['question_number']
        answer = q['correct_answer']
        answer_map[q_num] = answer
        print(f"Q{q_num:2d}: {answer}")

print(f"\nTotal: {len(answer_map)}/{data['total_questions']} questions have answers")
print("\nAll correct answers:")
print(json.dumps(answer_map, indent=2))
