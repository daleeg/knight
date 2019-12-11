#!/bin/bash

docker pull nginx:latest

docker pull redis:latest

docker pull mysql:5.7

docker pull python:3.5

pushd knight >/dev/null
docker build --rm -t knight:latest .
popd >/dev/null
