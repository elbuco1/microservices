FROM python:3.6-alpine

RUN adduser -D movies

WORKDIR /home/movies

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
# RUN venv/bin/pip install gunicorn

COPY app app
COPY movies.py config.py boot.sh ./
COPY .flaskenv ./

RUN chmod +x boot.sh

RUN chown -R movies:movies ./
USER movies

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]