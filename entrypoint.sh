#!/bin/bash
exec gunicorn --config ./source/configurations/gunicorn.py main
