from flask import render_template, request, flash, send_file, redirect
from io import BytesIO
from forms.seo_form import SeoForm
from models.seo_model import generate_seo_article

def generate_and_render():
    content_form=SeoForm()
    generated_content = None

    if content_form.validate_on_submit() and request.form.get('form_name') == 'content_form':
        topic = content_form.topic.data
        tone = content_form.tone.data
        word_count = content_form.word_count.data
        
        generated_content = generate_seo_article(topic, tone, word_count)
        flash("Tạo bài viết thành công!", "success")

    return render_template('index.html',
                           content_form=content_form,
                           generated_content=generated_content)

def download_text():
    content = request.form.get('content')  # Lấy nội dung từ form (tên trường là 'content')
    if content:
        buffer = BytesIO()  # Tạo bộ đệm để lưu nội dung dạng nhị phân
        buffer.write(content.encode('utf-8'))  # Ghi nội dung đã mã hóa UTF-8 vào bộ đệm
        buffer.seek(0)  # Đặt con trỏ về đầu file
        return send_file(  # Trả về file để người dùng tải xuống
            buffer,
            as_attachment=True,  # Gửi dưới dạng tệp đính kèm
            download_name='bai_viet_seo.txt',  # Tên file tải về
            mimetype='text/plain'  # Định dạng văn bản thuần
        )
    flash("Không có nội dung để tải!", "error")  # Hiển thị thông báo lỗi
    return redirect('/')  # Chuyển hướng về trang chủ
