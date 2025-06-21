

**Chatbot sinh bài viết SEO tự động sử dụng Gemini API 2.0-fast. Đơn giản, nhanh chóng, dễ dùng.**

---

## 1. Giới thiệu

`seo-gemini-chatbot` là một chatbot mã nguồn mở, giúp tự động sinh bài viết chuẩn SEO thông qua Gemini API 2.0-fast. Phù hợp cho các nhu cầu xây dựng website, blog cá nhân, hoặc dự án nội dung số.

---

## 2. Cấu hình

Tạo file `config.py` và thêm thông tin cấu hình như sau:

```python
class Config:
    SECRET_KEY = "YOUR_SECRET_KEY"
    GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
    GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key={GOOGLE_API_KEY}"
```
Lưu ý:

- Thay thế YOUR_SECRET_KEY và YOUR_GOOGLE_API_KEY bằng thông tin thực tế của bạn.

## 3. Cài đặt
Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```
## 4. Demo video
![Mô tả](https://github.com/HitDrama/seo-gemini-chatbot/blob/main/static/test.gif)

## 5. Thông tin người phát triển
Dev: Đặng Tố Nhân




