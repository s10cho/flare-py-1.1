#!/bin/sh

FLARE_HOME=$(cd "$(dirname "$0")" && cd ../;pwd)

# server run
cd $FLARE_HOME

if [ -f server.pid ]; then
	pid=`cat server.pid`
	kill $pid
	rm -f server.pid
	echo "server stop"
else
    PROCESS="ps -ef | grep python3 | grep server.py"
    proc=`eval $PROCESS`
    pid=`echo $proc | awk '{print $2}'`

    if [ -n "$pid" ]; then
        kill $pid
    fi
fi

python3 server.py 2>&1 &
echo $! > server.pid
echo "server start"