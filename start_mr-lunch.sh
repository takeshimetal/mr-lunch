#!/usr/bin/env bash

BASE_DIR=$(cd $(dirname $0);pwd)/

echo start mr-lunch
nohup pywatcher -t '.' -p '*.py' -c "python3 ${BASE_DIR}/run.py" &
