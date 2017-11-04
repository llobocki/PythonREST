from flask_restplus import Namespace, fields

api = Namespace('users', description='Users')

user = api.model('User', {
    'name': fields.String(required=True, description='The user name'),
    'surname': fields.String(required=True, description='The user name'),

})

response_user = api.clone('ResponseUser', user, {
    'id': fields.String(required=True, description='The user identifier'),

})


# user_parser = api.parser()
# user_parser.add_argument('name', type=str, required=True,
#                          help='User details', location='json')
# user_parser.add_argument('surname', type=str, required=True,
#                          help='User details', location='form')
#
# put_user_parser = user_parser.copy()
# post_user_parser = user_parser.copy()
