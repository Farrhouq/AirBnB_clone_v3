# api/v1/views/__init__.py

from flask import Blueprint

app_views = Blueprint('app_views', __name__)

# Import the views to register them with the Blueprint
from api.v1.views.index import *
# You would import other view modules similarly
