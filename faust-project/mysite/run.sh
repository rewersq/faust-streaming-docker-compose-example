#!/bin/sh
set -x

faust -A $WORKER worker --web-port=$WORKER_PORT
