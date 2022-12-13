#!/usr/bin/python3
import sqlalchemy
from models.base_model import engine, Contact, User, Rentor, Customers, Property, Image
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def contact_submission(title, email, feedback):
    try:
        contact = Contact(title=title, email=email, feedback=feedback)
        session.add(contact)
        session.commit()
        return 'Feedback added'
    except BaseException:
        session.rollback()
        raise


def signing_in(email):
    try:
        user = session.query(User).filter(User.email == email).first()
        if user is not None:
            return user.password
        else:
            return None
    except BaseException:
        # session.rollback()
        raise


def signing_up(username, full_name, phone_number, email, password):
    try:
        dbusername = session.query(User).filter(
            User.username == username).first()
        dbemail = session.query(User).filter(User.email == email).first()
        if dbusername is None:
            if dbemail is None:
                user = User(
                    username=username,
                    full_name=full_name,
                    phone_number=phone_number,
                    email=email,
                    password=password)
                session.add(user)
                session.commit()
                return 'User added'
            return 'Please Use another email'
        return 'Please Use another username'
    except BaseException:
        session.rollback()
        raise


def get_user_id(email):
    try:
        user = session.query(User).filter(User.email == email).first()
        if user is not None:
            return user.user_id
        else:
            return None
    except BaseException:
        # session.rollback()
        raise


def get_user_role(email):
    try:
        user = session.query(User).filter(User.email == email).first()
        if user is not None:
            return user.role
        else:
            return None
    except BaseException:
        # session.rollback()
        raise


def get_user_details(user_id):
    try:
        user = session.query(User).filter(User.user_id == user_id).first()
        if user is not None:
            return user
        else:
            return None
    except BaseException:
        # session.rollback()
        raise


def get_rentor_details(rentor_id):
    try:
        rentor = session.query(Rentor).filter(
            Rentor.rentor_id == rentor_id).first()
        if rentor is not None:
            return rentor
        else:
            return None
    except BaseException:
        # session.rollback()
        raise


def get_user_name(email):
    try:
        user = session.query(User).filter(User.email == email).first()
        if user is not None:
            return user.full_name
        else:
            return None
    except BaseException:
        # session.rollback()
        raise


def get_all_users():
    try:
        users = session.query(User).all()
        if users is not None:
            return users
        else:
            return None
    except BaseException:
        # session.rollback()
        raise


def roles_edit(user_id, role):
    try:
        user = session.query(User).filter(User.user_id == user_id).first()
        if user is not None:
            user.role = role
            session.commit()
            return 'Role updated'
        else:
            return None
    except BaseException:
        session.rollback()
        raise


def delete_a_user(user_id):
    try:
        user = session.query(User).filter(User.user_id == user_id).first()
        if user is not None:
            session.delete(user)
            session.commit()
            return 'User deleted'
        else:
            return None
    except BaseException:
        session.rollback()
        raise


def addProperty(rentor_id, name, bedrooms, bathrooms, location, size_in_sqft, price, description, available, expiry_time):
    try:
        property = Property(rentor_id, name=name, bedrooms=bedrooms, bathrooms=bathrooms, location=location, size_in_sqft=size_in_sqft, price=price, description=description, available=available, expiry_time=expiry_time)
        session.add(property)
        session.commit()
        return 'Property added'
    except BaseException:
        session.rollback()
        raise

def get_rentor_info(user_id):
    try:
        rentor = session.query(Rentor).filter(Rentor.user_id == user_id).first()
        if rentor is not None:
            return rentor
        else:
            return None
    except BaseException:
        # session.rollback()
        raise

def add_rentor_info(user_id, id_number, loation):
    try:
        rentor = Rentor(user_id=user_id, id_number=id_number, location=loation)
        session.add(rentor)
        session.commit()
        return 'Rentor info added'
    except BaseException:
        session.rollback()
        raise


def check_role(email):
    try:
        user = session.query(User).filter(User.email == email).first()
        if user is not None:
            return user.role
        else:
            return None
    except BaseException:
        # session.rollback()
        raise
