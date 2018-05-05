from models import Database
from api.v1 import api_v1
from flask import jsonify, abort, request
from helpers.wikipedia_api import wiki_search_id
import time

# creating db session
db = Database()

@api_v1.route('/generate_link', methods=['POST'])
def generate_link():
    start = time.time()
    data = request.get_json()

    if data is None:
        return jsonify({'error':'Not in JSON format'}), 400
    
    if not data['raw_source_title']:
        return jsonify({'error': 'Missing name'}), 400
    if not data['raw_target_title']:
        return jsonify({'error': 'Missing raw_target_title'}), 400
    try:
        results = db.findTheWikiConnection(
            wiki_search_id(data['raw_source_title']),
            wiki_search_id(data['raw_target_title'])
        )
    except Exception as e:
        print(e)
        # results = e
        results = "error"

    end = time.time()
    if type(results) == str:
        return jsonify({
            'err': results,
            'computeTime': end - start
        }), 401
    else:
        return jsonify({
            'result': results,
            'resultLen': len(results),
            'computeTime': end - start
        }), 200
