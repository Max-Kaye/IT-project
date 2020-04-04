#!/bin/bash
git pull
docker build -f itp-docker/Dockerfile -t itp-app .
cd itp-docker
docker-compose down
docker-compose up -d

