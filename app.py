#!/usr/bin/python3
from datetime import datetime
from flask import Flask, flash, Blueprint, g, render_template, request, abort, session, url_for, redirect
from jinja2 import TemplateNotFound
from models.BuildingForm import LoginForm, SignupForm, ContactForm
from models.base_model import Base, engine
from models.model_function import contact_submission
from flask_login import LoginManager, login_user, logout_user, login_required, current_user


app = Flask(__name__)
app.secret_key = '26682bea5f914ef84a779f0a7a678432'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

now = datetime.now()


@app.errorhandler(404)
def error(error):
    name = "page"
    return render_template('404.html', name=name), 404


@app.before_first_request
def create_db():
    Base.metadata.create_all(bind=engine)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def register():

    form = SignupForm()

    if form.validate_on_submit():
        username = form.username.data
        firstName = form.fistName.data
        lastName = form.lastName.data
        email = form.email.data
        password = form.password.data


    return render_template('signup.html', form=form)

@app.route('/feedback', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        title = form.title.data
        email = form.email.data
        feedback = form.feedback.data

        contact = contact_submission(title, email, feedback)

        return render_template('feedback.html', contact=contact, form=form)

    return render_template('feedback.html', form=form)

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
