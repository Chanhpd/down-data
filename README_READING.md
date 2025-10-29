# ✅ HSK H10901 Reading Exam - HOÀN THÀNH

## 📊 Tổng quan

- **Đề thi**: H10901 Reading (阅读)
- **URL**: https://mandarinbean.com/h10901-reading/
- **Thời gian**: 17 phút
- **Tổng số**: 4 Parts, 20 câu hỏi (Q21-Q40)
- **Đáp án**: ✅ Tất cả 20 câu đều có correct_answer

## 🎯 Cấu trúc đề thi

### Part 1: 第一部分 (Q21-25) - TRUE/FALSE
- **Loại**: Đúng/Sai
- **Có ảnh**: ✅ (R1_1.png đến R1_5.png)
- **Hướng dẫn**: 判断对错 (Đánh giá đúng sai)

**Đáp án:**
- Q21: TRUE ✓
- Q22: FALSE ✓
- Q23: TRUE ✓
- Q24: FALSE ✓
- Q25: TRUE ✓

### Part 2: 第二部分 (Q26-30) - Matching Sentences to Images
- **Loại**: Ghép câu với ảnh
- **Options**: A-F (6 ảnh: R1_6.png đến R1_11.png)
- **Hướng dẫn**: 选词填空 - 为句子选择合适的图片

**Câu hỏi:**
- Q26: 你好，我能吃一块儿吗？(Nǐ hǎo, wǒ néng chī yí kuàir ma?) → **D** ✓
- Q27: 他们在买衣服呢。(Tāmen zài mǎi yīfu ne.) → **B** ✓
- Q28: 天气太热了，多吃些水果。(Tiānqì tài rè le, duō chī xiē shuǐguǒ.) → **E** ✓
- Q29: 来，我们看看里面是什么东西。(Lái, wǒmen kànkan lǐmiàn shì shénme dōngxi.) → **A** ✓
- Q30: 喂，你睡觉了吗？(Wéi, nǐ shuìjiào le ma?) → **F** ✓

### Part 3: 第三部分 (Q31-35) - Matching Q&A
- **Loại**: Ghép câu hỏi với câu trả lời
- **Options**: A-F (6 đáp án cố định)
- **Hướng dẫn**: 为问题选择正确的回答

**Options:**
- A: 医院 (Yīyuàn) - Hospital
- B: 下雨了 (Xià yǔ le) - It rained
- C: 我不认识她 (Wǒ bú rènshi tā) - I don't know her
- D: 7岁 (suì) - 7 years old
- E: 下个月 (Xià ge yuè) - Next month
- F: 好的，谢谢 (Hǎo de, xièxie) - OK, thanks

**Đáp án:**
- Q31: 那个人是谁？(Who is that person?) → **C** (我不认识她) ✓
- Q32: 他女儿多大了？(How old is his daughter?) → **D** (7岁) ✓
- Q33: 你的同学在哪儿工作？(Where does your classmate work?) → **A** (医院) ✓
- Q34: 昨天上午天气怎么样？(How was the weather yesterday morning?) → **B** (下雨了) ✓
- Q35: 你什么时候回国？(When will you return to your country?) → **E** (下个月) ✓

### Part 4: 第四部分 (Q36-40) - Fill in the Blank
- **Loại**: Điền từ vào chỗ trống
- **Options**: A-F (6 từ cố định)
- **Hướng dẫn**: 选词填空

**Options:**
- A: 坐 (zuò) - sit
- B: 前面 (qiánmiàn) - in front
- C: 没关系 (méi guānxi) - no problem
- D: 名字 (míngzi) - name
- E: 汉语 (Hànyǔ) - Chinese language
- F: 月 (yuè) - month

**Đáp án:**
- Q36: 昨天是8（ ）19日 → **F** (月) ✓
- Q37: 那个饭馆儿在火车站（ ） → **B** (前面) ✓
- Q38: 你会说（ ）吗？ → **E** (汉语) ✓
- Q39: 在，请（ ），我去叫他 → **A** (坐) ✓
- Q40: （ ），我也刚到 → **C** (没关系) ✓

## 🚀 Cách sử dụng

### Bước 1: Tạo structure JSON
```bash
python crawl_reading.py
```

### Bước 2: Thêm đáp án
```bash
python add_reading_answers.py
```

### Bước 3: Kết quả
File `output_reading.json` với:
- ✅ 4 Parts đầy đủ
- ✅ 20 câu hỏi (Q21-Q40)
- ✅ Tất cả có correct_answer
- ✅ 11 ảnh (R1_1.png đến R1_11.png)
- ✅ Text tiếng Trung + Pinyin

## 📁 Cấu trúc JSON

```json
{
  "exam_url": "https://mandarinbean.com/h10901-reading/",
  "exam_title": "H10901 Reading",
  "exam_type": "reading",
  "time_limit_minutes": 17,
  "total_parts": 4,
  "total_questions": 20,
  "parts": [
    {
      "part_number": 1,
      "question_type": "TRUE_FALSE",
      "questions": [
        {
          "question_number": 21,
          "question_text": "Question 21",
          "image": "https://.../R1_1.png",
          "options": [...],
          "correct_answer": "TRUE"
        }
      ]
    }
  ]
}
```

## 🔗 So sánh với Listening

| Feature | Listening (H10901) | Reading (H10901) |
|---------|-------------------|------------------|
| Câu hỏi | Q1-Q20 | Q21-Q40 |
| Parts | 4 | 4 |
| Thời gian | 15 phút | 17 phút |
| Audio | ✅ 1 file MP3 | ❌ |
| Ảnh | 10 ảnh | 11 ảnh |
| File output | `output.json` | `output_reading.json` |

## 📝 Scripts

1. ✅ `crawl_reading.py` - Tạo structure JSON cho Reading
2. ✅ `add_reading_answers.py` - Thêm 20 correct_answer
3. ✅ `output_reading.json` - Kết quả cuối cùng (729 lines)

## 🎓 Sử dụng chung với Listening

Bạn có thể merge cả 2 đề thi vào 1 API:

```json
{
  "exam_id": "H10901",
  "sections": {
    "listening": {
      "questions": "Q1-Q20",
      "file": "output.json"
    },
    "reading": {
      "questions": "Q21-Q40", 
      "file": "output_reading.json"
    }
  }
}
```

## ✅ Status

- **Listening**: ✅ COMPLETE (20/20 questions with answers)
- **Reading**: ✅ COMPLETE (20/20 questions with answers)
- **Total**: 40 câu hỏi HSK Level 1

---

**Created**: October 29, 2025  
**Ready for**: Production API
