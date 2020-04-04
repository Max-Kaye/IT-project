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

## Deploy

Uses docker-compose - see [here](itp-docker/README.md)

    chmod +x deploy.sh
    ./deploy.sh

Then go to https://timesheets.maxant.ch

# Continuous Deployment
 
In order to automatically deploy when Jenkins touches the `dodeploy_itp.txt` file in it's home folder, run the script:

     chmod +x watch_for_dodeploy.sh
     nohup ./watch_for_dodeploy.sh > /dev/null 2>&1 &
     nohup ./watch_for_dodeploy.sh > watch_for_dodeploy.log 2>&1 &

It writes it's process ID to  `dodeploy_itp.pid`. Ideally you'd install this script as a service.

