from models import db
from api.v1 import api_v1
from flask import jsonify, abort, request


@app_views.route('/generate_link', methods=['PUT'])
def generate_link():
    data = request.get_json()

    if data is None:
        return jsonify({'error':'Not in JSON format'}), 400
    
    if not data['raw_source_title'] or not data['raw_target_title']:
        