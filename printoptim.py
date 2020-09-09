import os
import sys

from dotenv import load_dotenv

from flask import Flask

app = Flask(__name__)

app_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(app_root)

dotenv_path = os.path.join(app_root, '.env')
load_dotenv(dotenv_path)


@app.route("/")
def hello():
    return "hello"


if __name__ == "__main__":
    app.run("localhost", 5000)