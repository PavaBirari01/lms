import bcrypt
import psycopg2
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

app.config['SECRET_KEY']='thisisfirstflaskapp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pavan1@localhost/profiles'

conn = psycopg2.connect(
   database="profiles", user='postgres', password='pavan1'
)
cursor = conn.cursor()

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
from final_flask import routes
