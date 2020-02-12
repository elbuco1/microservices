from app import app
from flask import Flask, render_template
from flask import jsonify, make_response
from flask import request, abort
import logging as lg 

import app.utils as ut


@app.route('/', methods=['GET'])
def index():
    return "hello world"


# @app.route('/movies/all', methods=['GET'])
# @app.route('/movies', methods=['GET'])
# @app.route('/movies/', methods=['GET'])
# @app.route('/', methods=['GET'])

# def all_movies():
#     movies = ut.get_movies()
#     if len(movies) == 0:
#         abort(404)
#     return make_response(jsonify({"movies":movies}),200)


# @app.route('/movies/<movie_id>', methods=['GET'])
# def movie(movie_id):
#     movie = ut.get_movie(movie_id)
#     if movie is None:
#         abort(404)
#     return make_response(jsonify({"movie": movie}),200)


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


# @app.route('/movies/update/<movie_id>', methods=['PUT'])
# @app.route('/movies/<movie_id>', methods=['PUT'])
# def update_movie(movie_id):
#     requested_fields = {'name', 'year'}
#     included_fields = set(request.json.keys())

#     movie = ut.get_movie(movie_id)
#     if movie is None:
#         abort(404)

#     if not request.json:
#         abort(400)

#     if not ut.test_intersection(requested_fields,included_fields):
#         abort(400)

#     movie_name = request.json['name']
#     movie_year = request.json['year']

#     included_fields = set(request.json.keys())
#     movie = ut.update_movie_by_id(movie_id,movie_name,movie_year)
#     return make_response(jsonify(movie))

# @app.route('/movies/delete/<movie_id>', methods=['DELETE'])
# @app.route('/movies/<movie_id>', methods=['DELETE'])
# def del_movie(movie_id):
#     movie = ut.get_movie(movie_id)
#     if movie is None:
#         abort(404)
#     ut.delete_movie_by_id(movie_id)
#     # res = make_response(jsonify({"Deleted":True}), 204)
#     return jsonify({"Deleted":True})

# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)

# @app.errorhandler(400)
# def bad_request(error):
#     return make_response(jsonify({'error': 'Bad Request'}), 400)


# if __name__ == "__main__":
#     app.run(port=5000, debug=True)