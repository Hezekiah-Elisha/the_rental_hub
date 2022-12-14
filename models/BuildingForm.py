#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, \
    SelectField, FileField, DateTimeField, IntegerField, MultipleFileField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    fullname = StringField('First Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    # role = SelectField('Role', choices=[('admin', 'Admin'), ('user', 'User')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class ContactForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    feedback = TextAreaField('feedback', validators=[DataRequired()])
    submit = SubmitField('submit')


class RoleForm(FlaskForm):
    user_id = IntegerField('user_id', validators=[DataRequired()])
    role = SelectField(
        'Role',
        choices=[
            ('admin',
             'Admin'),
            ('customer',
             'Customer'),
            ('rentor',
             'Rentor'),
            ('agent',
             'Agent')])
    submit = SubmitField('submit')


class AddPropertyForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    bedrooms = IntegerField('bedrooms', validators=[DataRequired()])
    bathrooms = IntegerField('bathrooms', validators=[DataRequired()])
    size_in_sqft = IntegerField('size_in_sqft', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    price = IntegerField('price', validators=[DataRequired()])
    category = SelectField(
        'category',
        choices=[
            ('house',
             'House'),
            ('apartment',
             'Apartment'),
            ('land',
             'Land'),
            ('office',
             'Office')])
    availability = SelectField(
        'availability',
        choices=[
            ('available', 'Available'),
            ('unavailable', 'Unavailable')])

    # image = FileField('image', validators=[FileRequired(), FileAllowed(
        # ['jpg', 'png', 'Images only!'])])
    # images = MultipleFileField('images', validators=[FileRequired(), FileAllowed(
        # ['jpg', 'png', 'Images only!'])])
    # expiry_date = DateTimeField('expiry_date', validators=[DataRequired()])
    submit = SubmitField('submit')


class RentorCompleteForm(FlaskForm):
    id_number = IntegerField('id_number', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    submit = SubmitField('submit')


class EcoForm(FlaskForm):
    eco_friendly = SelectField(
        'eco_friendly',
        choices=[
            ('yes','Yes'),
            ('no','No')])
    green_energy = SelectField(
        'green_energy',
        choices=[
            ('yes','Yes'),
            ('no','No')])
    solar_panels = SelectField(
        'solar_panels',
        choices=[
            ('yes','Yes'),
            ('no','No')])
    rain_water_harvesting = SelectField(
        'rain_water_harvesting',
        choices=[
            ('yes','Yes'),
            ('no','No')])
    green_materials = SelectField(
        'green_materials',
        choices=[
            ('yes','Yes'),
            ('no','No')])
    description = TextAreaField('description', validators=[DataRequired()])
    submit = SubmitField('submit')

