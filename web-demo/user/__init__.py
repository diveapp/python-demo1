from flask import Flask

app = Flask(__name__)

from user import routes
