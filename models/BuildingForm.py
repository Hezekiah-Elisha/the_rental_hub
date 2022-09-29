#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, \
    SelectField, FileField, DateTimeField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired


class LoginForm(FlaskForm):
    pass


class RegisterForm(FlaskForm):
    pass


class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    feedback = TextAreaField('feedback', validators=[DataRequired()])
    submit = SubmitField('submit')
