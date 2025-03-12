from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError

class MyForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')

    def validate_password(self, field):
        if field.data:
            if len(field.data) < 8:
                raise ValidationError("Password must be at least 8 characters long")

    def validate_email(self, field):
        if field.data:
             if "@" not in field.data or "." not in field.data:
                raise ValidationError("Invalid email address")