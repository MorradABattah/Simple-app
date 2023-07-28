#!/bin/bash
docker build -t morradbattah/myapp:1.0.0 .
docker swarm init
docker stack deploy -c docker-compose.yml myapp
