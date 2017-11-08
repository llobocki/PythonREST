import json
from test.test import AppTest

from app.modules.user import models


class UserTest(AppTest):

    def test_put_404(self):
        body = {
            "name": "2",
            "surname": "3"
        }
        response = self.app.put(
            '/api/users/' + str(1),
            data=json.dumps(body),
            content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_delete_404(self):
        response = self.app.delete(
            '/api/users/' + str(1),
        )
        self.assertEqual(response.status_code, 404)

    def test_get_404(self):
        response = self.app.get(
            '/api/users/' + str(1),
        )
        self.assertEqual(response.status_code, 404)

    def test_post_400(self):
        body = {
            "name": "1",
        }
        response = self.app.post(
            '/api/users/',
            data=json.dumps(body),
            content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_get_list_empty(self):
        response = self.app.get('/api/users/')
        result = self._to_json(response.data)
        self.assertTrue(len(result) == 0)

    def test_post(self):
        body = {
            "name": "1",
            "surname": "1"
        }
        response = self.app.post(
            '/api/users/',
            data=json.dumps(body),
            content_type='application/json')
        self.assertEqual(response.status_code, 201)
        result = self._to_json(response.data)
        result.pop('id')
        self.assertDictEqual(result, body)

    def test_put_400(self):
        user = models.User(name="aaa", surname="bbb")
        self.db_session.add(user)
        self.db_session.commit()
        put_id = user.id
        body = {
            "name": "2",
        }
        response = self.app.put(
            '/api/users/' + str(put_id),
            data=json.dumps(body),
            content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.db_session.delete(user)
        self.db_session.commit()

    def test_put(self):
        user = models.User(name="aaa", surname="bbb")
        self.db_session.add(user)
        self.db_session.commit()
        put_id = user.id
        body = {
            "name": "2",
            "surname": "3"
        }
        response = self.app.put(
            '/api/users/' + str(put_id),
            data=json.dumps(body),
            content_type='application/json')
        result = self._to_json(response.data)
        result.pop('id')
        self.assertDictEqual(result, body)
        self.db_session.delete(user)
        self.db_session.commit()

    def test_get(self):
        expected_result = {"name": "aaa", "surname": "bbb"}
        user = models.User(name="aaa", surname="bbb")
        self.db_session.add(user)
        self.db_session.commit()
        put_id = user.id

        response = self.app.get(
            '/api/users/' + str(put_id),
        )
        result = self._to_json(response.data)
        result.pop('id')
        self.assertDictEqual(result, expected_result)

        self.db_session.delete(user)
        self.db_session.commit()

    def test_delete(self):
        user = models.User(name="aaa", surname="bbb")
        self.db_session.add(user)
        self.db_session.commit()
        put_id = user.id
        response = self.app.delete(
            '/api/users/' + str(put_id),
        )
        self.assertEqual(response.status_code, 204)

    def test_get_list(self):
        user_1 = models.User(name="aaa", surname="bbb")
        self.db_session.add(user_1)
        user_2 = models.User(name="aaa", surname="bbb")
        self.db_session.add(user_2)
        self.db_session.commit()

        response = self.app.get('/api/users/')
        result = self._to_json(response.data)
        self.assertTrue(len(result) == 2)
        self.db_session.delete(user_1)
        self.db_session.delete(user_2)
        self.db_session.commit()
