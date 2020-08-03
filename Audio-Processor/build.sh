#!/bin/sh

docker-compose build
docker run audiop  -p 5000:5000 hj/audiop
