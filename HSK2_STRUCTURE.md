# HSK Level 2 - Structure Complete ✅

## 🎉 Đã tạo xong cấu trúc HSK 2!

### 📊 So sánh HSK 1 vs HSK 2

| Feature | HSK 1 | HSK 2 |
|---------|-------|-------|
| **Listening Questions** | 20 câu (Q1-Q20) | 35 câu (Q1-Q35) ⭐ |
| **Reading Questions** | 20 câu (Q21-Q40) | 25 câu (Q36-Q60) ⭐ |
| **Total Questions** | 40 câu | 60 câu ⭐ |
| **Listening Time** | 15 phút | 25 phút |
| **Reading Time** | 17 phút | 22 phút |
| **Total Time** | 32 phút | 47 phút ⭐ |
| **Listening Parts** | 4 parts | 4 parts |
| **Reading Parts** | 4 parts | 4 parts |

## 📝 Cấu trúc chi tiết HSK 2

### Listening (35 câu, 25 phút)

#### Part 1: Q1-Q10 (10 câu)
- **Loại**: TRUE/FALSE
- **Format**: Nghe câu và xác định đúng/sai
- **Khác HSK 1**: 10 câu thay vì 5 câu

#### Part 2: Q11-Q25 (15 câu) ⭐ MỚI
- **Loại**: Multiple Choice Dialogue (A-F, 6 options)
- **Format**: Nghe đoạn hội thoại và chọn đáp án
- **Sub-parts**:
  - Q11-15: 5 câu
  - Q16-20: 5 câu (tương tự Q11-15)
  - Q21-25: 5 câu (pattern khác)
- **Khác HSK 1**: Part 2 của HSK 1 chỉ có 5 câu (Q6-Q10)

#### Part 3: Q26-Q30 (10 câu) ⭐ MỚI
- **Loại**: Multiple Choice Text (A-C)
- **Format**: Nghe đoạn văn ngắn và trả lời câu hỏi
- **Khác HSK 1**: HSK 1 có matching (A-F), HSK 2 có comprehension

#### Part 4: Q31-Q35 (5 câu)
- **Loại**: Comprehension (A-C)
- **Format**: Nghe đoạn hội thoại/văn dài và trả lời câu hỏi
- **Khác HSK 1**: HSK 1 có fill-in-blank với text Tiếng Trung

### Reading (25 câu, 22 phút)

#### Part 1: Q36-Q40 (5 câu)
- **Loại**: Sentence-Picture Match (A-B)
- **Format**: Xem ảnh và chọn câu mô tả đúng
- **Khác HSK 1**: HSK 1 là TRUE/FALSE với ảnh

#### Part 2: Q41-Q45 (5 câu)
- **Loại**: Sentence Completion (A-C)
- **Format**: Chọn từ điền vào chỗ trống
- **Tương tự HSK 1**: Part 4 của HSK 1

#### Part 3: Q46-Q50 (5 câu)
- **Loại**: Dialogue Completion (A-C)
- **Format**: Chọn câu phù hợp để hoàn thành đoạn hội thoại
- **Khác HSK 1**: HSK 1 là matching Q&A với 6 options cố định

#### Part 4: Q51-Q60 (10 câu) ⭐
- **Loại**: Reading Comprehension (A-C)
- **Format**: Đọc đoạn văn và trả lời câu hỏi
- **Khác HSK 1**: Nhiều câu hơn và phức tạp hơn

## 📁 File đã tạo

- ✅ `H20901_complete.json` (1428 lines)
  - Listening: 35 câu (Q1-Q35)
  - Reading: 25 câu (Q36-Q60)
  - Total: 60 câu

## 🎯 Điểm khác biệt chính

### 1. Số lượng câu hỏi
- **HSK 1**: 40 câu (nhẹ nhàng hơn)
- **HSK 2**: 60 câu (tăng 50%)

### 2. Độ phức tạp
- **HSK 1**: Câu hỏi đơn giản, nhiều ảnh, matching cơ bản
- **HSK 2**: Dialogue dài hơn, comprehension, ít ảnh hơn

### 3. Part 2 Listening
- **HSK 1**: 5 câu simple multiple choice
- **HSK 2**: 15 câu với 6 options (A-F), chia làm 3 sub-parts

### 4. Reading Comprehension
- **HSK 1**: 5 câu fill-in-blank
- **HSK 2**: 10 câu đọc hiểu với đoạn văn dài

## 🚀 Sử dụng

### Load HSK 2 exam:

```python
import json

with open('H20901_complete.json', 'r', encoding='utf-8') as f:
    hsk2_exam = json.load(f)

print(f"Level: HSK {hsk2_exam['exam_level']}")
print(f"Total: {hsk2_exam['total_questions']} questions")
print(f"Time: {hsk2_exam['total_time_minutes']} minutes")

# Access sections
listening = hsk2_exam['sections'][0]
reading = hsk2_exam['sections'][1]

print(f"Listening: {listening['total_questions']} questions")
print(f"Reading: {reading['total_questions']} questions")
```

### API Endpoints:

```javascript
// Get HSK 2 exam
GET /api/hsk2/exam/H20901
→ Returns H20901_complete.json

// Get listening section only
GET /api/hsk2/exam/H20901/listening
→ Returns 35 listening questions

// Get reading section only  
GET /api/hsk2/exam/H20901/reading
→ Returns 25 reading questions

// Get specific question
GET /api/hsk2/exam/H20901/question/15
→ Returns question 15 (Part 2 listening)
```

## 📝 Tiếp theo

### Để có đáp án thật:

1. Crawl thực tế từ trang web (cần Selenium vì JS-heavy)
2. Hoặc nhập thủ công vào file

### Để tạo thêm đề HSK 2:

```python
# Edit crawl_hsk2.py
exam_ids = ["H20901", "H20902", "H20903"]
```

## ✅ Tổng kết

- ✅ Đã tạo structure HSK 2 (60 câu)
- ✅ Khác biệt rõ ràng với HSK 1 (40 câu)
- ✅ Sẵn sàng cho API multi-level
- ⚠️ Cần đáp án thật cho production

---

**Created**: October 29, 2025  
**Status**: ✅ STRUCTURE COMPLETE  
**File**: H20901_complete.json (1428 lines)
