#!/bin/bash
app="ddos-realtime-monitor"
docker build -t ${app} .
docker run -v /etc/localtime:/etc/localtime:ro -d --restart unless-stopped -p 8080:80 \
  --name=${app} \
  -v $PWD/app ${app}