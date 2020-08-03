#!/bin/sh
docker-compose build
docker run --name=engine  -p 5001:5000 hj/engine
