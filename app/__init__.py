import os
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'V_Tornadus'
from app import views_ext

