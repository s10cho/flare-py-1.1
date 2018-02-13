#!/bin/sh

FLARE_HOME=$(cd "$(dirname "$0")" && cd ../;pwd)

echo "Argument Count : $#"
echo "Argument 1 : $1"
echo "Argument 2 : $2"


# run flare
cd $FLARE_HOME
python3 flare.py $*