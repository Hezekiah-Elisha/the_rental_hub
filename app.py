#!/usr/bin/python3
from datetime import datetime
from flask import Flask, flash, Blueprint, g, render_template, request, abort, session, url_for, redirect
from jinja2 import TemplateNotFound
from models.BuildingForm import LoginForm, SignupForm, ContactForm, RoleForm
from models.base_model import Base, engine
from models.model_function import contact_submission, signing_up, signing_in, get_user_id, get_user_role, get_user_name, get_all_users, \
    roles_edit, delete_a_user
from routes.user import user
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = '26682bea5f914ef84a779f0a7a678432'

app.register_blueprint(user)

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
        email = form.email.data
        password = form.password.data

        user = signing_in(email)
        if user is not None:
            if check_password_hash(user, password):
                session['email'] = email
                session['password'] = password
                session['logged_in'] = True
                session['full_name'] = get_user_name(email)
                return redirect('/dashboard')

            else:
                flash('Incorrect password', 'danger')
        else:
            flash('Email not found', 'danger')

    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def register():

    form = SignupForm()

    if form.validate_on_submit():
        username = form.username.data
        fullName = form.fullname.data
        phone = form.phone.data
        email = form.email.data
        password = form.password.data

        user = signing_up(
            username.strip().lower(),
            fullName.title(),
            phone,
            email.strip().lower(),
            generate_password_hash(password))
        flash(user, 'success')
        # flash(f"Account created for {form.username.data} of email {form.email.data}!", 'success')
        # return render_template('signup.html', user=user, form=form)

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


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/all_users', methods=['GET', 'POST'])
def all_user():
    users = get_all_users()
    return render_template('all_users.html', users=users)


@app.route('/add_house', methods=['GET', 'POST'])
def add_house():
    return render_template('add_house.html')


@app.route('/get_session', methods=['GET', 'POST'])
def get_session():
    return "some session"


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')


@app.route('/delete_user/<id>', methods=['GET', 'POST'])
def delete_user(id):
    user = delete_a_user(id)
    return redirect('/all_users')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)
