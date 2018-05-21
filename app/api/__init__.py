from flask import Blueprint
from app import docs


bp = Blueprint('api', __name__)


from app.api import users
