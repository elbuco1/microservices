import os

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    # evaluations_url = "132.207.72.45:8081"
    evaluations_url = "evaluations:8081"

    
    # Uncomment the desired option
    deploy = 'docker'   # deploying on docker using mysql
    # deploy = 'mysql_local' # deploying locally using mysql
    # deploy = 'sqlite_local' # deploying locally using sqlite

    SQLALCHEMY_DATABASE_URI = ''

    if deploy == 'docker':
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://movies:movies@db_movies/movies'
    elif deploy == 'mysql_local':
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://movies:movies@localhost:3306/movies'
    elif deploy == 'sqlite_local':
        SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    else:
        print("Wrong deployment option.")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

