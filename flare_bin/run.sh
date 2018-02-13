#!/bin/sh

FLARE_HOME=$(cd "$(dirname "$0")" && cd ../;pwd)

# run flare
cd $FLARE_HOME
python3 flare.py $1 $2