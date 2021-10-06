#!/usr/bin/env bash

git clone git@github.com:ebot7/python-coding-challenge-test.git
image_id=$(docker build --no-cache -q . | awk -F':' '{print $2}')
docker run $image_id /bin/sh -c 'cd python-coding-challenge-test && python test_suite.py'
