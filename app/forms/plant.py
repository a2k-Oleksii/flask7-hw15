from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class RegistrationForm(FlaskForm):
    title = StringField("Title")
    location = StringField("Location")
    submit = SubmitField("Register")


class ProfileForm(FlaskForm):
    title = StringField("Title")
    location = StringField("Location")
    submit = SubmitField("Register")
