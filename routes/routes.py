from flask import Blueprint
from controllers.seo_controller import generate_and_render, download_text

# Tạo Blueprint
seo_router = Blueprint("seo", __name__)

# Đăng ký route bằng cách truyền hàm vào sau .route()
seo_router.route("/", methods=["GET", "POST"])(generate_and_render)
seo_router.route("/download_text", methods=["POST"])(download_text)
