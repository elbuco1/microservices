FROM python:3.6-alpine

RUN adduser -D evaluations

WORKDIR /home/evaluations

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY evaluations.py config.py boot.sh ./
COPY .flaskenv ./

RUN chmod +x boot.sh

RUN chown -R evaluations:evaluations ./
USER evaluations

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]


# sudo docker build -t evaluations:latest .