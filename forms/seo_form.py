from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class SeoForm(FlaskForm):
    topic = StringField('Chủ đề bài viết', validators=[DataRequired()])
    tone = SelectField('Phong cách', choices=[
        ('formal', 'Chính thức'),
        ('casual', 'Thân mật'),
        ('persuasive', 'Thuyết phục')
    ], validators=[DataRequired()])
    word_count = IntegerField('Số từ', validators=[DataRequired(), NumberRange(min=300, max=3000)])
    submit = SubmitField('Tạo bài viết')
