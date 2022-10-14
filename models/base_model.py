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
    __tablename__ = "admin"
    admin_id = Column(Integer, nullable=False, primary_key=True)
    username = Column(String(200), nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(255), nullable=False)
    reg_time = Column(DateTime, default=datetime.now, nullable=False)


class Vendor(Base):
    '''
    Table User: for the user table
    '''
    __tablename__ = 'users'
    user_id = Column(Integer, nullable=False, primary_key=True)
    username = Column(String(200), nullable=False)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
    reg_time = Column(DateTime, default=datetime.now, nullable=False)


class Client(Base):
    '''
    Table Client: Intance of Base for table clients
    '''
    __tablename__ = 'clients'
    client_id = Column(Integer, nullable=False, primary_key=True)
    username = Column(String(200), nullable=False)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
    reg_time = Column(DateTime, default=datetime.now, nullable=False)


class Building(Base):
    '''
    Table Building: Instance of Base for table building
    '''
    __tablename__ = "buildings"
    building_id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(200), nullable=False)
    rooms = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    expiry_time = Column(DateTime, default=datetime.now, nullable=True)
    reg_time = Column(DateTime, default=datetime.now, nullable=False)

