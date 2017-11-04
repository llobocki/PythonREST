import config
# from app import blueprint as api
from app import create_app
from flask import Flask

# from app.database import init_db

# app = Flask(__name__)
# app.register_blueprint(api)

app = create_app(config)

app.run(host='0.0.0.0', port=8081)
