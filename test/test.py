import json
import os
import tempfile
import unittest

import config
from app import create_app


def to_json(data):
    return json.loads(data.decode('utf-8'))


class FlaskrTest(unittest.TestCase):

    def setUp(self):
        self.db_fd, database_path = tempfile.mkstemp()
        config.SQLALCHEMY_DATABASE_URI = 'sqlite:///' + database_path
        api = create_app(config)
        self.app = api.test_client()

    def tearDown(self):
        os.close(self.db_fd)

    def test_user(self):
        response = self.app.get('/api/users/')
        result = to_json(response.data)
        self.assertTrue(len(result) == 0)

        body = {
            "name": "1",
        }
        response = self.app.post(
            '/api/users/',
            data=json.dumps(body),
            content_type='application/json')
        self.assertEqual(response.status_code, 400)

        body = {
            "name": "1",
            "surname": "1"
        }
        response = self.app.post(
            '/api/users/',
            data=json.dumps(body),
            content_type='application/json')
        self.assertEqual(response.status_code, 201)
        result = to_json(response.data)
        result.pop('id')
        self.assertDictEqual(result, body)

        body = {
            "name": "2",
            "surname": "2"
        }
        response = self.app.post(
            '/api/users/',
            data=json.dumps(body),
            content_type='application/json')
        self.assertEqual(response.status_code, 201)
        result = to_json(response.data)
        put_id = result.pop('id')
        self.assertDictEqual(result, body)

        body = {
            "name": "2",
        }
        response = self.app.put(
            '/api/users/' + str(put_id),
            data=json.dumps(body),
            content_type='application/json')
        result = to_json(response.data)
        self.assertEqual(response.status_code, 400)

        body = {
            "name": "2",
            "surname": "3"
        }
        response = self.app.put(
            '/api/users/' + str(put_id),
            data=json.dumps(body),
            content_type='application/json')
        result = to_json(response.data)
        result.pop('id')
        self.assertDictEqual(result, body)

        response = self.app.get(
            '/api/users/' + str(put_id),
        )
        result = to_json(response.data)
        result.pop('id')
        self.assertDictEqual(result, body)

        response = self.app.get('/api/users/')
        result = to_json(response.data)
        self.assertTrue(len(result) == 2)

        response = self.app.delete(
            '/api/users/' + str(put_id),
        )
        self.assertEqual(response.status_code, 204)

        response = self.app.delete(
            '/api/users/' + str(put_id),
        )
        self.assertEqual(response.status_code, 404)

        response = self.app.get(
            '/api/users/' + str(put_id),
        )
        self.assertEqual(response.status_code, 404)

        body = {
            "name": "2",
            "surname": "3"
        }
        response = self.app.put(
            '/api/users/' + str(put_id),
            data=json.dumps(body),
            content_type='application/json')
        self.assertEqual(response.status_code, 404)

        response = self.app.get('/api/users/')
        result = to_json(response.data)
        self.assertTrue(len(result) == 1)


if __name__ == '__main__':
    unittest.main()
