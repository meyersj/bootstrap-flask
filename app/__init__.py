import os, sys

from flask import Flask
from flask.ext.cors import CORS

app = Flask(__name__)
app.config.from_object('config')
app.debug = True
CORS(app)

from app import views
