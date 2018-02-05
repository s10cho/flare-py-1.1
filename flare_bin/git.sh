#!/bin/sh

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
cd $SCRIPT_DIR

FLARE_HOME=`cd ../;pwd`
cd $FLARE_HOME

git pull

find . -name "*.py" -exec chmod -v 755 {} \;

cd $SCRIPT_DIR

find . -name "*.sh" -exec chmod -v 755 {} \;