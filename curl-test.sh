#/bin/bash

curl http://localhost:5000/api/timeline_post

random_string=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 16)

curl -X POST http://localhost:5000/api/timeline_post -d "name=name_${random_string}&email=email_${random_string}&content=content_${random_string}"

curl http://localhost:5000/api/timeline_post
