from api.v1 import api_v1
from flask import jsonify


@api_v1.route('/ping')
def pulse_check():
    return jsonify({"status": "Pong!"})

