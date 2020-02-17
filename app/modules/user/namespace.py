from flask_restx import Namespace, fields

api = Namespace('users', description='Users')

user = api.model('User', {
    'name': fields.String(required=True, description='The user name'),
    'surname': fields.String(required=True, description='The user name'),

})

response_user = api.clone('ResponseUser', user, {
    'id': fields.String(required=True, description='The user identifier'),

})
