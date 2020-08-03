#!/bin/sh
docker-compose build
docker run --name=audiop  -p 5000:5000 hj/audiop
