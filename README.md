# IT-project

## GitHub Build

![Python application](https://github.com/Max-Kaye/IT-project/workflows/Python%20application/badge.svg)

## Background

- uses Python 2.7 because of students using Windows XP

## Install

    pip install -r requirements.txt

(stores stuff in `/usr/local/lib/python2.7/dist-packages` on Linux)

## Test

    export MYSQL_PASSWORD=<the password>
    python -m unittest discover -s app -p "*_test.py"

## Run

Set the environment variables MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT!
(all have defaults except for the password)

    python2.7 app/main.py

Then point your browser to http://localhost:8080/

