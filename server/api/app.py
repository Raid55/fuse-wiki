#!/usr/bin/python3
import socket
from models import db
from os import getenv
from api import api_v1
from flask import Flask, make_response, jsonify

app = Flask(__name__)


app.register_blueprint(api_v1, url_prefix='/v1')


@app.teardown_appcontext
def close_method(exception):
    db.close()

@app.errorhandler(404)
def not_found(err):
    return make_response(jsonify({"error": "There is nothing here..."}), 404)

if __name__ == "__main__":
    try:
        host_name = socket.gethostname()
        app_host = socket.gethostbyname(host_name)
    except:
        app_host = getenv('API_HOST')
        if app_host is None:
            app_host = '0.0.0.0'
    
    app_port = getenv('API_PORT')
    if app_port is None:
        app_port = 8080
    
    app.run(host=app_host, port=int(app_port))
