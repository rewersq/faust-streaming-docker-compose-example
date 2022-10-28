#!/bin/sh
set -x

export SIMPLE_SETTINGS=settings

faust --app $WORKER worker --web-port=$WORKER_PORT
