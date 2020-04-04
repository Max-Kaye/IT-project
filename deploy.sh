#!/bin/bash

# remove all local changes - eg. previous changes to the javascript regarding build time
git checkout -- .
git pull

# add build time to application
TIME=$(date +%Y%m%d_%H%M%S)
echo "console.log('Build time: $TIME');" >> web/code.js

# build the image
docker build -f itp-docker/Dockerfile -t itp-app .

# bounce servers and use new image
cd itp-docker
docker-compose down
docker-compose up -d

