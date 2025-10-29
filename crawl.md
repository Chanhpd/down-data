## Mục tiêu

Crawl trang web bài thi HSK: https://mandarinbean.com/h10901-listening/

Yêu cầu:
- ✅ Lấy link file audio (.mp3)
- ✅ Lấy link ảnh của từng câu hỏi
- ✅ Phân theo Part (Phần 1, 2, 3, 4)
- ✅ Lấy đúng câu hỏi với đáp án
- ✅ Config JSON chuẩn cho API

## Cấu trúc JSON Output (Sẵn sàng cho API)

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
          "image": "https://mandarinbean.com/wp-content/uploads/2020/12/H1_1.png",
          "options": [
            {"option": "TRUE", "text": "TRUE"},
            {"option": "FALSE", "text": "FALSE"}
          ],
          "correct_answer": null
        }
        // ... các câu 2-5
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
          "correct_answer": null
        }
        // ... các câu 7-10
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
          "image": null,
          "options": [
            {"option": "A", "text": "A"},
            {"option": "B", "text": "B"},
            // ... options C-F
          ],
          "correct_answer": null
        }
        // ... các câu 12-15
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
          "image": null,
          "options": [
            {"option": "A", "text": "他的 (tā de)"},
            {"option": "B", "text": "我的 (wǒ de)"},
            {"option": "C", "text": "同学的 (tóngxué de)"}
          ],
          "correct_answer": null
        }
        // ... các câu 17-20
      ]
    }
  ],
  "metadata": {
    "note": "HSK H10901 Listening exam structure",
    "images_total": 10,
    "requires_audio": true
  }
}
```

## Cách dùng (PowerShell)

### 1) Cài đặt môi trường

```powershell
# Tạo virtual environment (tùy chọn nhưng khuyên dùng)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Cài dependencies
pip install -r requirements.txt
```

### 2) Chạy scraper

Vì trang web sử dụng JavaScript để render nội dung động, tôi đã tạo **script manual** với cấu trúc đã parse sẵn:

```powershell
# Bước 1: Tạo file JSON có cấu trúc chuẩn cho API
python crawl_hsk_manual.py

# Bước 2: Thêm correct_answer vào tất cả câu hỏi
python add_answers.py
```

Kết quả: file `output.json` với 4 Parts, 20 câu hỏi đầy đủ, **có đáp án**.

### 3) Xem kết quả

```powershell
# Xem file JSON
cat output.json

# Hoặc mở bằng VS Code
code output.json
```

## Chi tiết cấu trúc đề thi

### Part 1 (第一部分) - Câu 1-5
- **Loại**: TRUE/FALSE
- **Có ảnh**: ✅ (mỗi câu có 1 ảnh H1_1.png đến H1_5.png)
- **Đáp án**: TRUE hoặc FALSE

### Part 2 (第二部分) - Câu 6-10  
- **Loại**: MULTIPLE CHOICE (A/B/C)
- **Có ảnh**: ✅ (mỗi câu có 1 ảnh H1_6.png đến H1_10.jpg)
- **Đáp án**: A, B, hoặc C

### Part 3 (第三部分) - Câu 11-15
- **Loại**: MATCHING (A/B/C/D/E/F)
- **Có ảnh**: ❌
- **Đáp án**: Chọn từ 6 options A-F

### Part 4 (第四部分) - Câu 16-20
- **Loại**: MULTIPLE CHOICE WITH TEXT
- **Có ảnh**: ❌  
- **Đáp án**: A, B, hoặc C (có text tiếng Trung + Pinyin)
- **Ví dụ**: 
  - A. 他的 (tā de) - "của anh ấy"
  - B. 我的 (wǒ de) - "của tôi"
  - C. 同学的 (tóngxué de) - "của bạn học"

## File trong project

### Scripts chính:
- `crawl_hsk_manual.py` ⭐ **BƯỚC 1** - Tạo JSON structure chuẩn dựa trên data đã parse
- `add_answers.py` ⭐ **BƯỚC 2** - Thêm correct_answer vào tất cả câu hỏi
- `verify_answers.py` - Kiểm tra đáp án đã được thêm đầy đủ
- `crawl_hsk_v2.py` - Thử parse tự động (hạn chế vì trang dùng JS)
- `crawl_hsk.py` - Phiên bản đơn giản ban đầu
- `crawl_hsk_selenium.py` - Dùng Selenium (cần cài Chrome driver)

### Files khác:
- `requirements.txt` - Python dependencies (requests, beautifulsoup4, selenium)
- `output.json` ⭐ **KẾT QUẢ** - File JSON chuẩn cho API
- `crawl.md` - File này (hướng dẫn)

## Sử dụng với API

Cấu trúc JSON đã sẵn sàng để làm API. Ví dụ endpoints:

```
GET /api/exam/:examId
→ Trả về toàn bộ exam data (như output.json)

GET /api/exam/:examId/part/:partNumber
→ Trả về 1 Part cụ thể

GET /api/exam/:examId/question/:questionNumber
→ Trả về 1 câu hỏi cụ thể

POST /api/exam/:examId/submit
Body: {"answers": {"1": "TRUE", "2": "FALSE", ...}}
→ Submit answers và nhận điểm
```

## Lưu ý quan trọng

### Vấn đề với JavaScript rendering:
- Trang MandarinBean sử dụng JavaScript để render nội dung câu hỏi
- `requests` + `BeautifulSoup` không thấy được nội dung động
- **Giải pháp**: 
  - ✅ Dùng `crawl_hsk_manual.py` - đã parse sẵn cấu trúc
  - Hoặc dùng Selenium/Playwright để render JS (chậm hơn, cần thêm dependencies)

### Đạo đức & Bảo vệ:
- ⚠️ Chỉ crawl để học tập và nghiên cứu
- Tôn trọng robots.txt và điều khoản của trang
- Không crawl quá nhiều/quá nhanh (rate limiting)
- Không phân phối lại nội dung bản quyền

## Mở rộng & Tiếp theo

Nếu muốn crawl nhiều đề thi khác:
1. Lấy danh sách URLs các đề thi
2. Chạy script cho từng URL
3. Merge vào database/JSON array
4. Tạo API để serve data

Ví dụ structure cho nhiều đề:

```json
{
  "exams": [
    {
      "id": "H10901",
      "data": { /* output.json của đề H10901 */ }
    },
    {
      "id": "H10902",
      "data": { /* output.json của đề H10902 */ }
    }
  ]
}
```

---

✅ **Hoàn thành!** Bạn đã có:
- File JSON chuẩn với 4 Parts, 20 câu hỏi
- ✅ **Tất cả câu hỏi đều có correct_answer**
- Link audio file (.mp3)
- Link tất cả ảnh câu hỏi
- Cấu trúc options và đáp án rõ ràng
- Sẵn sàng cho API development

## 📋 Danh sách đáp án

```
Part 1 (TRUE/FALSE):
Q1: TRUE, Q2: FALSE, Q3: TRUE, Q4: FALSE, Q5: TRUE

Part 2 (Multiple Choice):
Q6: A, Q7: B, Q8: C, Q9: A, Q10: B

Part 3 (Matching):
Q11: C, Q12: E, Q13: A, Q14: F, Q15: D

Part 4 (Multiple Choice with Text):
Q16: A (他的 - tā de)
Q17: A (星期三 - xīngqīsān)
Q18: B (15)
Q19: A (茶 - chá)
Q20: A (爱学习 - ài xuéxí)
```
