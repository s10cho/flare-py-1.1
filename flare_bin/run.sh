#!/bin/sh

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
echo $SCRIPT_DIR
cd $SCRIPT_DIR

FLARE_HOME=`cd ../;pwd`
echo $FLARE_HOME
cd $FLARE_HOME

python3 flare.py $1