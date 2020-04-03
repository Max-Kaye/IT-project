# taken from https://hub.docker.com/_/python
# build with, from the project root folder:
#            docker build -f itp-docker/Dockerfile -t itp-app .
#
FROM python:2.7.17-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY web web
COPY sql sql
COPY app app

EXPOSE 8080

CMD [ "python", "./app/main.py" ]
