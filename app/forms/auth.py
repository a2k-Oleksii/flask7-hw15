from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    user_identifier = StringField("Username or Email", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last name")
    username = StringField("Username", [DataRequired(), Length(4, 255)])
    email = StringField("Email Address", [DataRequired(), Email()])
    password = PasswordField("Password", [DataRequired(), Length(8, 255)])
    password_confirm = PasswordField("Confirm Password", [DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

    def validate_username(self, form, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("This username is taken.")

    def validate_email(self, form, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("This email is already registred.")


class ProfileForm(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last name")
    username = StringField("Username", [DataRequired(), Length(4, 255)])
    email = StringField("Email Address", [DataRequired(), Email()])
    submit = SubmitField("Register")
