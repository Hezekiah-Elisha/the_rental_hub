#!/usr/bin/python3
from datetime import datetime
from flask import Flask, flash, Blueprint, g, render_template, request, abort, session, url_for, redirect
from jinja2 import TemplateNotFound
from models.BuildingForm import LoginForm, RegisterForm, ContactForm

app = Flask(__name__)
app.secret_key = '26682bea5f914ef84a779f0a7a678432'

now = datetime.now()


@app.errorhandler(404)
def error(error):
    name = "page"
    return render_template('404.html', name=name)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        firstName = form.fistName.data
        lastName = form.lastName.data
        email = form.email.data
        password = form.password.data


    return render_template('register.html', form=form)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        feedback = form.feedback.data

    return render_template('contact.html', form=form)

@app.route('/add_house', methods=['GET', 'POST'])
def add_house():
    return render_template('add_house.html')


@app.route('/get_session', methods=['GET', 'POST'])
def get_session():
    return "some session"


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('admin/dashboard.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)
