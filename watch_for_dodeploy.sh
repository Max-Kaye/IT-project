#!/bin/bash

OLD_PID=$(cat watch_for_dodeploy.pid)
if [ -z "$OLD_PID" ]
then
  echo "no old process to kill"
else
  echo "old process needs killing: $OLD_PID"
  kill $OLD_PID
  echo "killed old process"
fi

echo this process has PID $$

echo "MYSQL Env: "
env | grep MYSQL

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

