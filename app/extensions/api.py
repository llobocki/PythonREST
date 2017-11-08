from app.modules.user.controllers import api as user_api
from flask import Blueprint
from flask_restplus import Api

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint,
          title='API',
          version='1.0',
          description='API',
          )

api.add_namespace(user_api)
