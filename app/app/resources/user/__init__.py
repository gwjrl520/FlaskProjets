from flask import Blueprint
from flask import current_app
from flask_restful import Api

from commons.settings.extensions import apispec
from app.resources.user.user import UserResource
from app.resources.user.user import UserList


user_bp = Blueprint('', __name__, url_prefix='/api/v1')
user_api = Api(user_bp, '/users')

user_api.add_resource(UserResource, '/user')
user_api.add_resource(UserList, '/user/<user_id>')


@user_bp.before_app_first_request
def register_views():
    apispec.spec.path(view=UserResource, app=current_app)
    apispec.spec.path(view=UserList, app=current_app)