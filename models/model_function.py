#!/usr/bin/python3
import sqlalchemy
from models.base_model import engine, Contact, Admin, Rentor, Customers, Property, Image
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
