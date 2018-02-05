#!/bin/sh

FLARE_HOME=$(cd "$(dirname "$0")" && cd ../;pwd)

cd $FLARE_HOME
python3 flare.py $1