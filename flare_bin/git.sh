#!/bin/sh

FLARE_HOME=`cd ../;pwd`

cd $FLARE_HOME
git pull
find . -name "*.py" -exec chmod -v 755 {} \;