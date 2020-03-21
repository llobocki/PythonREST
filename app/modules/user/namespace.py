from flask_restx import Namespace, fields

api = Namespace('users', description='Users')

user = api.model('User', {
    'id': fields.Integer(readonly=True, description='The user identifier'),
    'name': fields.String(required=True, description='The user name'),
    'surname': fields.String(required=True, description='The user name'),

})
