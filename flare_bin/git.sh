#!/bin/sh

FLARE_HOME=$(cd "$(dirname "$0")" && cd ../;pwd)
FLARE_BIN_DIR=$(cd "$(dirname "$0")" && pwd)

# git pull & *.py chomd change
cd $FLARE_HOME
git pull
find . -name "*.py" -exec chmod -v 755 {} \;

# *.sh chomd cnange
cd $FLARE_BIN_DIR
find . -name "*.sh" -exec chmod -v 755 {} \;