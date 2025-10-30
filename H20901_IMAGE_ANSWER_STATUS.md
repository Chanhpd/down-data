# H20901 - Image và Answer Status

## ✅ Đã cập nhật thành công!

### 📸 Image URLs đã thêm:

#### Listening Section:
- **Part 2 (Q11-Q20)**: 10 images ✅
  - Pattern: `H20901_L2_{11-20}.jpg`
  - URL: `https://learnchinese.mandarinbean.com/wp-content/uploads/H20901_L2_XX.jpg`

#### Reading Section:
- **Part 1 (Q36-Q40)**: 5 images ✅
  - Pattern: `H20901_R1_{36-40}.jpg`
  - URL: `https://learnchinese.mandarinbean.com/wp-content/uploads/H20901_R1_XX.jpg`

### 📝 Correct Answer Field:

✅ **Đã thêm `correct_answer` cho tất cả 60 câu**
- Listening: Q1-Q35 (35 câu)
- Reading: Q36-Q60 (25 câu)

⚠️ **Hiện tại tất cả `correct_answer` đều là `""` (empty string)**

### 🎯 Phân bố Image theo Part:

| Section | Part | Questions | Has Images? | Count |
|---------|------|-----------|-------------|-------|
| **Listening** | Part 1 | Q1-Q10 | ❌ No | 0 |
| **Listening** | Part 2 | Q11-Q20 | ✅ Yes | 10 |
| **Listening** | Part 3 | Q21-Q30 | ❌ No | 0 |
| **Listening** | Part 4 | Q31-Q35 | ❌ No | 0 |
| **Reading** | Part 1 | Q36-Q40 | ✅ Yes | 5 |
| **Reading** | Part 2 | Q41-Q45 | ❌ No | 0 |
| **Reading** | Part 3 | Q46-Q50 | ❌ No | 0 |
| **Reading** | Part 4 | Q51-Q60 | ❌ No | 0 |

**Tổng images**: 15 ảnh (10 Listening + 5 Reading)

## 📋 Sample JSON Structure:

### Question với image (Q11):
```json
{
  "question_number": 11,
  "question_text": "Question 11",
  "dialogue": null,
  "image_url": "https://learnchinese.mandarinbean.com/wp-content/uploads/H20901_L2_11.jpg",
  "options": [
    {"option": "A", "text": "A"},
    {"option": "B", "text": "B"},
    {"option": "C", "text": "C"},
    {"option": "D", "text": "D"},
    {"option": "E", "text": "E"},
    {"option": "F", "text": "F"}
  ],
  "correct_answer": ""
}
```

### Question không có image (Q1):
```json
{
  "question_number": 1,
  "question_text": "Question 1",
  "image": null,
  "options": [
    {"option": "TRUE", "text": "TRUE"},
    {"option": "FALSE", "text": "FALSE"}
  ],
  "correct_answer": null
}
```

## 🚀 Tiếp theo để hoàn thiện:

### 1. Điền đáp án thực:
Bạn cần điền đáp án vào file. Có 2 cách:

#### Cách 1: Edit thủ công JSON
```json
"correct_answer": "A"  // Thay "" thành "A", "B", "TRUE", etc.
```

#### Cách 2: Tạo script với answer key
```python
answers = {
    1: "TRUE",
    2: "FALSE",
    3: "TRUE",
    # ... tiếp tục cho 60 câu
}
```

### 2. Verify Image URLs:
Kiểm tra xem images có thực sự tồn tại không:
- Mở browser và test: `https://learnchinese.mandarinbean.com/wp-content/uploads/H20901_L2_11.jpg`
- Nếu không load được, cần adjust pattern

### 3. Crawl nội dung thực:
Để có:
- `question_text`: Câu hỏi tiếng Trung thật
- `dialogue`: Đoạn hội thoại
- `passage`: Đoạn văn
- `options.text`: Text đáp án thật

## 📊 File Stats:

- **File**: `H20901_complete.json`
- **Size**: 1443 lines (tăng từ 1428 lines)
- **Total Questions**: 60
- **Questions with Images**: 15 (25%)
- **Questions with Answers**: 0 (0%) - need to fill
- **Structure**: Complete ✅
- **Image URLs**: Complete ✅ (for applicable questions)
- **Answer Keys**: Pending ⏳

## ✅ Checklist:

- [x] Add `correct_answer` field to all 60 questions
- [x] Add image URLs for Listening Part 2 (Q11-Q20)
- [x] Add image URLs for Reading Part 1 (Q36-Q40)
- [ ] Fill in actual answer keys (A, B, C, TRUE, FALSE, etc.)
- [ ] Verify image URLs are accessible
- [ ] Crawl actual Chinese text for questions and options
- [ ] Add dialogues and passages content

---

**Last Updated**: October 30, 2025  
**Status**: ✅ STRUCTURE + IMAGES COMPLETE | ⏳ ANSWERS PENDING
