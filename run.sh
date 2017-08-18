#!/usr/bin/env bash

export FLASK_APP=hello-world.py
python -m flask run -h 0.0.0.0 -p 80
