import os
import sys
import json

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

from flask import Flask

postgres_user = os.getenv("DB_USER")
postgres_password = os.getenv("DB_PASSWORD")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{postgres_user}:{postgres_password}@localhost"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(app_root)

dotenv_path = os.path.join(app_root, '.env')
load_dotenv(dotenv_path)

db = SQLAlchemy(app)
db.init_app(app)


@app.route("/")
def hello():
    return "hello"


@app.route("/create_user", methods=["POST"])
def create_view_user():
    return json.dumps({
        "test": "ok",
    })


if __name__ == "__main__":
    app.run("localhost", 5000)
