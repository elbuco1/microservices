# from src.models.movies import Movie
# import src.models.movies as m

from app.models import Evaluation
from app import db

import logging as lg 


def test_intersection(set_a, set_b):
    intersection = set_a.intersection(set_b) 
    return intersection == set_a



# def get_movie_year_by_name(movie_name, Movie):
#     movies = Movie.query.filter(Movie.name == movie_name).all()
#     movie = movies[0]
#     return str(movie.year)

def get_evaluations():
    evaluations = Evaluation.query.all()
    evaluations = [e.serialize() for e in evaluations]
    return evaluations

def get_evaluations_movie_id(movie_id):
    evaluations = Evaluation.query.filter(Evaluation.movie_id == movie_id).all()
    evaluations = [e.serialize() for e in evaluations]
    return evaluations


def get_evaluation(evaluation_id):
    evaluation = db.session.query(Evaluation).get(evaluation_id)
    # return evaluation.serialize()
    return evaluation




def add_evaluation(description,movie_id):
    evaluation = Evaluation(description,movie_id)
    db.session.add(evaluation)
    db.session.commit()
    # movies = Movie.query.filter(Movie.id == movie.id)
    # return db.session.query(Evaluation).get(evaluation.id).serialize()
    return db.session.query(Evaluation).get(evaluation.id)




def delete_evaluation_by_id(evaluation_id):
    evaluation = Evaluation.query.filter(Evaluation.id == evaluation_id).first()
    db.session.delete(evaluation)
    db.session.commit()

def update_evaluation_by_id(evaluation_id,description):
    x = db.session.query(Evaluation).get(evaluation_id)
    x.description = description
    db.session.commit()
    # return x.serialize()
    return x
