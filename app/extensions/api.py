from flask import Blueprint, Flask
from flask_restplus import Api, apidoc

from app.modules.user.controllers import api as user_api

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint,
          title='API',
          version='1.0',
          description='API',
          )

api.add_namespace(user_api)
