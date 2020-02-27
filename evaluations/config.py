import os

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    movies_url = "http://127.0.0.1:8000"
    # movies_url = "http://127.0.0.1:5000"

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

