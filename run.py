import config
from app import create_app

app = create_app(config)

app.run(host='0.0.0.0', port=8081)
