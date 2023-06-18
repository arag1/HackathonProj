#!/bin/sh
export FLASK_APP=./hackathon/index.py
pipenv run flask --debug run -h 0.0.0.0