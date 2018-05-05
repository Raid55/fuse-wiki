#!/usr/bin/python3
import socket
# from models import db
from os import getenv
from api.v1 import api_v1
from flask import Flask, make_response, jsonify
from raven.contrib.flask import Sentry
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.register_blueprint(api_v1, url_prefix='/v1')

sentry = Sentry(app, dsn=getenv('SENTRY_DSN'))

# @app.teardown_appcontext
# def close_method(exception):
#     db.close()

@app.errorhandler(404)
def not_found(err):
    return make_response(jsonify({"error": "There is nothing here..."}), 404)

@app.route("/", methods=['GET'])
def root_test():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app_host = '0.0.0.0'
    app.run(host=app_host,)
