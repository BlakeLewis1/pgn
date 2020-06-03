from flask import Flask, request
from flask_bcrypt import Bcrypt
import requests

app = Flask(__name__)

from application import routes