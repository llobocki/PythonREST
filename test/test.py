import json
import os
import tempfile
import unittest

import config
from app import create_app


class AppTest(unittest.TestCase):

    def _to_json(self, data):
        return json.loads(data.decode('utf-8'))

    def setUp(self):
        self.db_fd, database_path = tempfile.mkstemp()
        config.SQLALCHEMY_DATABASE_URI = 'sqlite:///' + database_path
        api = create_app(config)
        self.app = api.test_client()

    def tearDown(self):
        os.close(self.db_fd)


if __name__ == '__main__':
    unittest.main()
