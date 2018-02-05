#!/bin/sh

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
cd $SCRIPT_DIR

FLARE_HOME=`cd ../;pwd`
cd $FLARE_HOME

python3 flare.py $1