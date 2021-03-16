# databaseCreation.py
# Author : Andre Baldo (http://github.com/andrebaldo/)
# Make sure that you have a SQL Server runing in your local host, check also the instance
# name, in some instalations the server path will be 'localhost/SQLEXPRESS' in this case, 
# update the SERVER variable below accordingly
# This script creates the tables User and UserSession, just execute:$python databaseCreation.py
# from your command pront, tested just on Windows.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#create the database then apply this python script
SERVER = 'LAPTOP-A84E5O9M\SQLEXPRESS'
DATABASE = 'chat_database'
DRIVER = 'SQL Server Native Client 11.0'
DATABASE_CONNECTION = f'mssql://{SERVER}/{DATABASE}?trusted_connection=yes&driver={DRIVER}'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION

db = SQLAlchemy(app)


import flask_login


class User(db.Model, flask_login.mixins.UserMixin):
    __tablename__ = 'chat_User' # Name of the table in our database
    # Defining the columns
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    mobilePhone = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    def get_id(self):
        return db.text_type(self.userId)



db.create_all()
db.session.commit()