#!/bin/sh
set -x

export SIMPLE_SETTINGS=settings
faust $WORKER worker --web-port=$WORKER_PORT
