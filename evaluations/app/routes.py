from app import app
from flask import Flask, render_template
from flask import jsonify, make_response
from flask import request, abort
import logging as lg 

import app.utils as ut


# @app.route('/', methods=['GET'])
# def index():
#     return "hello world"

@app.route('/', methods=['GET'])
@app.route('/evaluations', methods=['GET'])
@app.route('/evaluations/', methods=['GET'])
def all_evaluations():
    evaluations = ut.get_evaluations()
    if len(evaluations) == 0:
        abort(404)
    return make_response(jsonify({"evaluations":evaluations}),200)


@app.route('/evaluations/<evaluation_id>', methods=['GET'])
def evaluation(evaluation_id):
    evaluation = ut.get_evaluation(evaluation_id)
    if evaluation is None:
        abort(404)
    return make_response(jsonify({"evaluation": evaluation}),200)


# @app.route('/movies/add', methods=['POST'])
# @app.route('/movies', methods=['POST'])
# def create_movie():
#     requested_fields = {'name', 'year'}
#     included_fields = set(request.json.keys())
#     if not request.json or not ut.test_intersection(requested_fields,included_fields):
#         abort(400)
#     movie_name = request.json['name']
#     movie_year = request.json['year']

#     if request.method == 'POST':
#         movie = ut.add_movie(movie_name, movie_year)
#         return make_response(jsonify({"movie": movie}),201)


@app.route('/evaluations/update/<evaluation_id>', methods=['PUT'])
@app.route('/evaluations/<evaluation_id>', methods=['PUT'])
def update_evaluation(evaluation_id):
    requested_fields = {'description'}
    included_fields = set(request.json.keys())

    evaluation = ut.get_evaluation(evaluation_id)
    if evaluation is None:
        abort(404)

    if not request.json:
        abort(400)

    if not ut.test_intersection(requested_fields,included_fields):
        abort(400)

    description = request.json['description']

    included_fields = set(request.json.keys())
    evaluation = ut.update_evaluation_by_id(evaluation_id,description)
    return make_response(jsonify(evaluation))

@app.route('/evaluations/delete/<evaluation_id>', methods=['DELETE'])
@app.route('/evaluations/<evaluation_id>', methods=['DELETE'])
def del_evaluation(evaluation_id):
    evaluation = ut.get_evaluation(evaluation_id)
    if evaluation is None:
        abort(404)
    ut.delete_evaluation_by_id(evaluation_id)
    return jsonify({"Deleted":True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


# if __name__ == "__main__":
#     app.run(port=5000, debug=True)