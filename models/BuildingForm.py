#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, \
    SelectField, FileField, DateTimeField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    fullname = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class ContactForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    feedback = TextAreaField('feedback', validators=[DataRequired()])
    submit = SubmitField('submit')

class AddHouseForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('submit')


class AddPropertyForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('submit')


class AddImageForm(FlaskForm):
    image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('submit')

class AddRentorForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('submit')

class AddCustomerForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('submit')

class AddAgentForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('submit')

class AddAdminForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('submit')

class AddContactForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('submit')

class AddFeedbackForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    price = StringField('price', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('submit')
