import json
import database

from flask import Flask
app = Flask(__name__)


@app.route('/planets/')
def planets():
    return json.dumps(list(database.planets().keys()))
