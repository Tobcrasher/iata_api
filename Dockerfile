# syntax=docker/dockerfile:1


FROM python:3.8-slim-buster

ADD ./app/app.py /

RUN pip3 freeze > requirements.txt

RUN pip3 install -r requirements.txt

RUN pip3 install flask
RUN pip3 install flask-mysql
RUN pip3 install Flask-JSON
RUN pip3 install flask-cors
RUN pip3 install cryptography

CMD sleep 1m && python3 -m flask run --host='0.0.0.0'
