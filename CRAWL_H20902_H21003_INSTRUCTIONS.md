# Hướng dẫn crawl H20902 và H21003

## ✅ Đã tạo sẵn:
1. ✅ `H20902_complete.json` - Template với structure đầy đủ (chưa có answers)
2. ✅ `H21003_complete.json` - Template với structure đầy đủ (chưa có answers)
3. ✅ `parse_h20902_answers.py` - Script parse answers cho H20902
4. ✅ `parse_h21003_answers.py` - Script parse answers cho H21003
5. ✅ `verify_h20902.py` - Verify script
6. ✅ `verify_h21003.py` - Verify script

## 📋 Các bước thực hiện:

### Bước 1: Crawl H20902

1. Mở trình duyệt, vào: https://mandarinbean.com/h20902-listening/
2. Scroll xuống, click nút **"View Result"**
3. Sau khi trang load xong, **Ctrl+S** → Save as:
   - File name: `H20902 Listening - Mandarin Bean.html`
   - Save type: Web page, HTML only
   - Location: Folder `d:\Code\python\exam hsk\`

4. Vào: https://mandarinbean.com/h20902-reading/
5. Click **"View Result"**
6. **Ctrl+S** → Save as:
   - File name: `H20902 Reading - Mandarin Bean.html`
   - Location: Folder `d:\Code\python\exam hsk\`

7. Chạy lệnh:
   ```bash
   python parse_h20902_answers.py
   ```

8. Verify:
   ```bash
   python verify_h20902.py
   ```

### Bước 2: Crawl H21003

1. Mở trình duyệt, vào: https://mandarinbean.com/h21003-listening/
2. Click **"View Result"**
3. **Ctrl+S** → Save as: `H21003 Listening - Mandarin Bean.html`

4. Vào: https://mandarinbean.com/h21003-reading/
5. Click **"View Result"**
6. **Ctrl+S** → Save as: `H21003 Reading - Mandarin Bean.html`

7. Chạy lệnh:
   ```bash
   python parse_h21003_answers.py
   ```

8. Verify:
   ```bash
   python verify_h21003.py
   ```

## 🎯 Kết quả mong đợi:

Sau khi hoàn thành, bạn sẽ có:
- ✅ `H20902_complete.json` - 60 câu với đáp án đầy đủ
- ✅ `H21003_complete.json` - 60 câu với đáp án đầy đủ

## 🚀 Quick Commands:

```bash
# H20902
python parse_h20902_answers.py
python verify_h20902.py

# H21003
python parse_h21003_answers.py
python verify_h21003.py
```

## ⚠️ Lưu ý:

- File HTML phải được save **SAU KHI** click "View Result"
- File name phải chính xác (có dấu cách)
- Đảm bảo save vào đúng folder: `d:\Code\python\exam hsk\`
- Mỗi exam cần 2 files HTML (Listening + Reading)

## 📊 Progress Tracking:

- [x] H20901 ✅ DONE (60/60 answers)
- [ ] H20902 ⏳ PENDING (need HTML files)
- [ ] H21003 ⏳ PENDING (need HTML files)
