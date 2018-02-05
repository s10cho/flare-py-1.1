#!/bin/sh

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
echo $SCRIPT_DIR
cd $SCRIPT_DIR

FLARE_HOME=`cd ../;pwd`
echo $FLARE_HOME
cd $FLARE_HOME

git pull
find . -name "*.py" -exec chmod -v 755 {} \;