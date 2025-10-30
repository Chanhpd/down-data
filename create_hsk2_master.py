import json

# Create master HSK2 file combining all 3 exams
exams = ['H20901', 'H20902', 'H21003']
master_data = {
    "level": "HSK 2",
    "total_exams": 3,
    "total_questions": 180,
    "exams": []
}

for exam_id in exams:
    filename = f"{exam_id}_complete.json"
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            exam_data = json.load(f)
            master_data["exams"].append(exam_data)
            print(f"✅ Added {exam_id}: {exam_data['total_questions']} questions")
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")

# Save master file
with open('HSK2_all_exams.json', 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print("\n✅ Created HSK2_all_exams.json")
print(f"📊 Total: {master_data['total_exams']} exams, {master_data['total_questions']} questions")
