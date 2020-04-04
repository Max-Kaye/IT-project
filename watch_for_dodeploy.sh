#!/bin/bash
echo running as process $$
echo $$ > watch_for_dodeploy.pid
FILE="/w/jenkins/jenkins_home/dodeploy_itp.txt"
while true ; do
  echo "creating file to watch" \
  && touch $FILE \
  && inotifywait $FILE \
    && echo "deployment requested" \
    && ./deploy.sh \
    && echo "deployment completed" \
    && touch $FILE \
    && echo "waiting for next modify..."
done

