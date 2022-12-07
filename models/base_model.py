#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
from sqlalchemy import create_engine, ForeignKey, DateTime, Column, Integer, String, Boolean
from sqlalchemy.dialects.mysql import LONGTEXT

host = 'localhost'
user = 'root'
password = 'root'
database = 'the_rental_hub'

SQLALCHEMY_DATABASE_URL = f"mysql+mysqldb://{user}:{password}@{host}/{database}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, echo=True)
session = sessionmaker(bind=engine)

Base = declarative_base()


class Contact(Base):
    '''
    Table Contact: for info on feedback
    '''
    __tablename__ = "contacts"
    contact_id = Column(Integer, nullable=False, primary_key=True)
    title = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    feedback = Column(LONGTEXT, nullable=False)
    feedback_time = Column(DateTime, default=datetime.now, nullable=False)


class Admin(Base):
    '''
    Table Admin: for the admin table
    '''
    __tablename__ = "admins"
    admin_id = Column(Integer, nullable=False, primary_key=True)
    username = Column(String(200), nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(100), nullable=False)
    reg_time = Column(DateTime, default=datetime.now, nullable=False)


class Rentor(Base):
    '''
    Table User: for the user table
    '''
    __tablename__ = 'rentors'
    user_id = Column(Integer, nullable=False, primary_key=True)
    username = Column(String(200), nullable=False)
    full_name = Column(String(200), nullable=False)
    id_number = Column(String(200), nullable=False, unique=True)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
    reg_time = Column(DateTime, default=datetime.now, nullable=False)


class Customers(Base):
    '''
    Table Client: Intance of Base for table clients
    '''
    __tablename__ = 'customers'
    client_id = Column(Integer, nullable=False, primary_key=True)
    username = Column(String(200), nullable=False)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
    reg_time = Column(DateTime, default=datetime.now, nullable=False)


class Property(Base):
    '''
    Table Building: Instance of Base for table building
    '''
    __tablename__ = "properties"
    building_id = Column(Integer, nullable=False, primary_key=True)
    images_id = Column(Integer, ForeignKey('images.images_id'), nullable=False)
    rentor_id = Column(Integer, ForeignKey('rentors.user_id'), nullable=False)
    name = Column(String(200), nullable=False)
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=False)
    location = Column(String(200), nullable=False)
    size_in_sqft = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(LONGTEXT, nullable=False)
    available = Column(Boolean, default=True, nullable=False)
    expiry_time = Column(DateTime, default=datetime.now, nullable=True)
    reg_time = Column(DateTime, default=datetime.now, nullable=False)


class Image(Base):
    '''
    Table Image: Instance of Base for table image
    '''
    __tablename__ = "images"
    images_id = Column(Integer, nullable=False, primary_key=True)
    property_id = Column(Integer, ForeignKey('properties.building_id'), nullable=False)
    image_url = Column(String(200), nullable=False)
    image_name = Column(String(200), nullable=False)
    reg_time = Column(DateTime, default=datetime.now, nullable=False)



