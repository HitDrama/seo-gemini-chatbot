class Config:
    SECRET_KEY = YOUR_SECRET_KEY
    GOOGLE_API_KEY = YOUR_GOOGLE_API_KEY
    GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key={GOOGLE_API_KEY}"
