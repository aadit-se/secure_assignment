from flask import Flask,render_template, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
import os
import sqlite3
con = sqlite3.connect("database.db", check_same_thread=False)
# conn = sqlite3.connect('your.db')
cur=con.cursor()

# UPLOAD_FOLDER = os.path.join('../project/static')
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'sessionData'
app.config['TESTING'] = True
# app.config['PORT']=8000
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_ECHO'] = False
# app.config['SQLALCHEMY_RECORD_QUERIES'] = False
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/assignment3'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0
# db = SQLAlchemy(app)

# cur = con.cursor()

@app.route('/')
def index():
    return render_template('LoginPage.html')

from project.com.controller import ProjectAdminController