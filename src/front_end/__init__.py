from flask import Blueprint

front = Blueprint('front', __name__, static_folder='app')