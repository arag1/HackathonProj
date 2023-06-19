#!/bin/sh
export FLASK_APP=./hackathon/index.py
export FLASK_DEBUG=1
pipenv run flask run -h 0.0.0.0