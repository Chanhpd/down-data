# HSK Exam Crawler & API

Crawl và tạo API cho bài thi HSK từ MandarinBean.com

## 🎯 Tính năng

✅ **Listening Exam (H10901)** - 20 câu (Q1-Q20)  
✅ **Reading Exam (H10901)** - 20 câu (Q21-Q40)  
✅ Phân theo Part (4 Parts mỗi phần)  
✅ Lấy link audio file (.mp3) cho Listening  
✅ Lấy link ảnh từng câu hỏi  
✅ Parse đáp án và options đầy đủ  
✅ Export JSON chuẩn cho API  
✅ Example FastAPI implementation  
✅ **Tổng cộng: 40 câu hỏi HSK Level 1**

## 📦 Cài đặt

```bash
# Clone hoặc tải project
cd "exam hsk"

# Tạo virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows PowerShell

# Cài dependencies
pip install -r requirements.txt
```

## 🚀 Sử dụng

### 1. Crawl dữ liệu

**Listening Exam (Q1-Q20):**
```bash
# Bước 1: Tạo file JSON structure
python crawl_hsk_manual.py

# Bước 2: Thêm correct_answer
python add_answers.py

# Bước 3 (Optional): Verify
python verify_answers.py
```
Kết quả: `output.json` với 20 câu Listening

**Reading Exam (Q21-Q40):**
```bash
# Bước 1: Tạo file JSON structure
python crawl_reading.py

# Bước 2: Thêm correct_answer
python add_reading_answers.py
```
Kết quả: `output_reading.json` với 20 câu Reading

**Tổng cộng: 40 câu hỏi HSK Level 1 đầy đủ đáp án!**

### 2. Chạy API (Optional)

```bash
# Cài thêm FastAPI dependencies nếu chưa có
pip install fastapi uvicorn pydantic

# Chạy API server
python api_example.py
# hoặc
uvicorn api_example:app --reload
```

API sẽ chạy tại: `http://localhost:8000`

### 3. Test API

```bash
# Xem docs
open http://localhost:8000/docs

# Get full exam
curl http://localhost:8000/exam

# Get Part 1
curl http://localhost:8000/exam/part/1

# Get Question 1
curl http://localhost:8000/exam/question/1

# Submit answers
curl -X POST http://localhost:8000/exam/submit \
  -H "Content-Type: application/json" \
  -d '{"answers": {"1": "TRUE", "2": "FALSE", "6": "A"}}'
```

## 📁 Cấu trúc Project

```
exam hsk/
├── crawl.md                   # Hướng dẫn Listening (tiếng Việt)
├── README.md                  # File này
├── README_READING.md          # ⭐ Hướng dẫn Reading chi tiết
├── requirements.txt           # Python dependencies
│
├── output.json               # ⭐ Listening data (Q1-Q20) có đáp án
├── output_reading.json       # ⭐ Reading data (Q21-Q40) có đáp án
│
├── crawl_hsk_manual.py       # Tạo Listening JSON
├── add_answers.py            # Thêm đáp án Listening
├── verify_answers.py         # Verify Listening
│
├── crawl_reading.py          # ⭐ Tạo Reading JSON
├── add_reading_answers.py    # ⭐ Thêm đáp án Reading
│
├── crawl_hsk.py              # Script cơ bản (legacy)
├── crawl_hsk_v2.py           # Parse tự động (legacy)
├── crawl_hsk_selenium.py     # Dùng Selenium (legacy)
│
└── api_example.py            # Example FastAPI implementation
```

## 📊 Cấu trúc JSON Output

```json
{
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
          "image": "https://mandarinbean.com/.../H1_1.png",
          "options": [
            {"option": "TRUE", "text": "TRUE"},
            {"option": "FALSE", "text": "FALSE"}
          ],
          "correct_answer": null
        }
      ]
    }
  ]
}
```

## 🎓 Chi tiết các Part

| Part | Câu hỏi | Loại | Có ảnh | Options |
|------|---------|------|--------|---------|
| 1 | 1-5 | TRUE/FALSE | ✅ | TRUE, FALSE |
| 2 | 6-10 | Multiple Choice | ✅ | A, B, C |
| 3 | 11-15 | Matching | ❌ | A, B, C, D, E, F |
| 4 | 16-20 | Multiple Choice (Text) | ❌ | A, B, C + Chinese text |

## 🔌 API Endpoints

| Method | Endpoint | Mô tả |
|--------|----------|-------|
| GET | `/` | API info |
| GET | `/exam` | Full exam data |
| GET | `/exam/part/{part_number}` | Lấy 1 Part |
| GET | `/exam/question/{question_number}` | Lấy 1 câu hỏi |
| GET | `/exam/audio` | Link audio file |
| POST | `/exam/submit` | Submit answers & get score |

## 💡 Ví dụ Response

### GET /exam/question/16

```json
{
  "part": 4,
  "question": {
    "question_number": 16,
    "question_text": "Question 16",
    "image": null,
    "options": [
      {"option": "A", "text": "他的 (tā de)"},
      {"option": "B", "text": "我的 (wǒ de)"},
      {"option": "C", "text": "同学的 (tóngxué de)"}
    ],
    "correct_answer": null
  }
}
```

### POST /exam/submit

Request:
```json
{
  "answers": {
    "1": "TRUE",
    "2": "FALSE",
    "6": "A",
    "16": "A"
  }
}
```

Response:
```json
{
  "score": 15,
  "total": 20,
  "percentage": 75.0,
  "results": {
    "1": true,
    "2": true,
    "6": false,
    ...
  }
}
```

## ⚠️ Lưu ý

### Vấn đề JavaScript rendering
- Trang MandarinBean render nội dung bằng JavaScript
- `requests` + `BeautifulSoup` không đủ
- **Giải pháp**: Dùng `crawl_hsk_manual.py` với data đã parse sẵn
- Hoặc dùng Selenium (cần Chrome driver)

### Bảo mật & Production
- ⚠️ `correct_answer` hiện có trong JSON cho mục đích demo
- **Production**: Lưu đáp án trong database riêng, không expose cho client
- Chỉ trả về correct_answer sau khi user submit
- Validate answers ở backend

### Đạo đức
- Chỉ crawl để học tập
- Tôn trọng robots.txt
- Không phân phối nội dung bản quyền

## 🔧 Mở rộng

### Crawl nhiều đề thi

```python
exams = [
    "https://mandarinbean.com/h10901-listening/",
    "https://mandarinbean.com/h10902-listening/",
    # ...
]

all_data = []
for url in exams:
    data = crawl(url)
    all_data.append(data)

# Save to database or JSON
```

### Database Schema (PostgreSQL example)

```sql
CREATE TABLE exams (
    id SERIAL PRIMARY KEY,
    exam_id VARCHAR(20) UNIQUE,
    title VARCHAR(200),
    audio_url TEXT
);

CREATE TABLE parts (
    id SERIAL PRIMARY KEY,
    exam_id INTEGER REFERENCES exams(id),
    part_number INTEGER,
    title VARCHAR(100),
    description TEXT
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    part_id INTEGER REFERENCES parts(id),
    question_number INTEGER,
    question_text TEXT,
    image_url TEXT,
    correct_answer VARCHAR(10)
);

CREATE TABLE options (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions(id),
    option_letter VARCHAR(10),
    option_text TEXT
);
```

## 📚 Documentation

Xem thêm chi tiết trong `crawl.md` (tiếng Việt)

## 🤝 Contributing

Feel free to:
- Improve parsing logic
- Add more exam sources
- Enhance API features
- Fix bugs

## 📝 License

For educational purposes only. Respect original content copyright.

---

**Tạo bởi**: GitHub Copilot  
**Ngày**: 2025  
**Version**: 1.0.0
# down-data
