#!/bin/sh

MONITORING_HOME=$(cd "$(dirname "$0")" && cd ../;pwd)

##########################
# monitoring stop
##########################
cd $MONITORING_HOME/bin
if [ -f docker_monitoring.pid ]; then
	pid=`cat docker_monitoring.pid`
	kill $pid
	rm -f docker_monitoring.pid
	echo "docker monitoring stop"
fi
