# ⚠️ QUAN TRỌNG: Cách lấy HTML đúng

## ❌ SAI - HTML không có đáp án
Nếu bạn chỉ mở trang và save ngay → File HTML sẽ KHÔNG có đáp án

## ✅ ĐÚNG - HTML có đáp án đầy đủ

### Bước 1: Vào trang Listening
1. Mở: https://mandarinbean.com/h20902-listening/
2. Scroll xuống phần quiz
3. **QUAN TRỌNG**: Click nút **"View Result"** (hoặc "Submit" nếu có)
4. Đợi trang load xong → Sẽ thấy đáp án màu xanh
5. Bây giờ mới **Ctrl+S** (hoặc Right click → Save as)
6. Save as: `H20902 Listening - Mandarin Bean.html`
7. Location: `d:\Code\python\exam hsk\` (KHÔNG phải folder html/)

### Bước 2: Vào trang Reading
1. Mở: https://mandarinbean.com/h20902-reading/
2. Scroll xuống phần quiz
3. **QUAN TRỌNG**: Click nút **"View Result"**
4. Đợi thấy đáp án màu xanh
5. **Ctrl+S** → Save as: `H20902 Reading - Mandarin Bean.html`
6. Location: `d:\Code\python\exam hsk\`

### Bước 3: Parse answers
```bash
python parse_h20902_answers.py
```

### Bước 4: Verify
```bash
python verify_h20902.py
```

---

## 🔍 Cách kiểm tra HTML đã đúng chưa:

Mở file HTML bằng text editor, search chuỗi: `correct-answer`

- ✅ **Có tìm thấy** → File đúng, có đáp án
- ❌ **Không tìm thấy** → File sai, chưa click "View Result"

## 📋 Làm tương tự cho H21003:

1. https://mandarinbean.com/h21003-listening/ → View Result → Save
2. https://mandarinbean.com/h21003-reading/ → View Result → Save
3. `python parse_h21003_answers.py`
4. `python verify_h21003.py`

---

## 🎯 Checkpoint:

Sau khi làm xong, bạn sẽ có:
- ✅ `H20902_complete.json` với 60/60 answers
- ✅ `H21003_complete.json` với 60/60 answers

## 💡 Tips:

- Nếu trang yêu cầu login → Có thể cần tài khoản premium
- Nếu không thấy nút "View Result" → Thử scroll xuống cuối trang
- File HTML phải > 500KB thì mới đúng (file có đáp án sẽ lớn hơn)
