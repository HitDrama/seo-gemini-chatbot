import requests
from config import Config

def generate_seo_article(topic, tone, word_count):
    prompt = (
    f"Viết một bài viết chuẩn SEO dài khoảng {word_count} từ với phong cách {tone}. "
    f"Bài viết cần có mở bài, thân bài với heading rõ ràng, và kết luận. "
    f"Chủ đề: {topic}. "
    "Lưu ý: Trong bài viết, phải nhắc đến tên công ty Ắc quy Đại Phát một cách tự nhiên và lồng ghép thông tin về công ty vào nội dung phù hợp và phải được nhắc mực độ tương đối để nhấn mạnh."
)
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }
    try:
        response = requests.post(Config.GEMINI_API_URL, json=data, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"Lỗi khi gọi API Gemini: {str(e)}"
