#!/bin/bash

PROJECT_DIR="/root/flask-website-template"

cd "$PROJECT_DIR" || exit

git fetch
git checkout joshua-dierickse
git reset origin/joshua-dierickse --hard

docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build
