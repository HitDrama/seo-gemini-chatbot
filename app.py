from config import Config
from routes.routes import seo_router
from flask import Flask

app = Flask(__name__)
app.config.from_object(Config)

# Đăng ký route
app.register_blueprint(seo_router)

if __name__ == '__main__':
    app.run(debug=True)
