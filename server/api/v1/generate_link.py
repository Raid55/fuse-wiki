from models import Database
from api.v1 import api_v1
from flask import jsonify, abort, request
from helpers.b_dir_earch import findTheWikiConnection
from helpers.wikipedia_api import wiki_search_id

# creating db session
db = Database()

@api_v1.route('/generate_link', methods=['POST'])
def generate_link():
    data = request.get_json()

    if data is None:
        return jsonify({'error':'Not in JSON format'}), 400
    
    if not data['raw_source_title']:
        return jsonify({'error': 'Missing name'}), 400
    if not data['raw_target_title']:
        return jsonify({'error': 'Missing raw_target_title'}), 400

    return jsonify({
            'result': db.test( 
                wiki_search_id(data['raw_source_title']),
                wiki_search_id(data['raw_target_title'])
            )
        }), 200
