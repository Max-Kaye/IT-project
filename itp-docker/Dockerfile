# taken from https://hub.docker.com/_/python
# build with:
#            docker build -t itp-app .
#
FROM python:2.7.17-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
