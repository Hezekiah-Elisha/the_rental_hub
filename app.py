#!/usr/bin/python3
from datetime import datetime
from flask import Flask, g, render_template, request, abort, session, url_for, redirect
from jinja2 import TemplateNotFound
from models.BuildingForm import LoginForm, RegisterForm, ContactForm

app = Flask(__name__)
app.secret_key = '26682bea5f914ef84a779f0a7a678432'

now = datetime.now()


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)
