#!/bin/sh
set -x

$WORKER worker --web-port=$WORKER_PORT
