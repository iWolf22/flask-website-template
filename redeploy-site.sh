#!/bin/bash

PROJECT_DIR="/root/flask-website-template"
VENV_DIR="python3-virtualenv"

tmux kill-server

cd "$PROJECT_DIR"

git fetch
git checkout joshua-dierickse
git reset origin/joshua-dierickse --hard

source "$VENV_DIR/bin/activate"

pip install -r requirements.txt

systemctl restart myportfolio