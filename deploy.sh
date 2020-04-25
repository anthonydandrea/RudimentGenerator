#!/bin/bash

sudo docker tag rudiment-generator gcr.io/rudimentgenerator/rudiment-generator

rm ~/.docker/config.json
sudo docker login
gcloud auth print-access-token | sudo docker login -u oauth2accesstoken --password-stdin https://gcr.io

sudo docker push gcr.io/rudimentgenerator/rudiment-generator
