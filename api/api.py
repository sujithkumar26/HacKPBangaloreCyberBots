from flask import Flask
from apis import api
from flask_cors import CORS

from db import mongo

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = "mongodb://localhost:27017/VirtualPresence"

mongo.init_app(app)
api.init_app(app)

app.run(debug=True)
