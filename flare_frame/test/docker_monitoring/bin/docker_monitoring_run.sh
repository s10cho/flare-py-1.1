#!/bin/sh

MONITORING_HOME=$(cd "$(dirname "$0")" && cd ../;pwd)
LOG_DIRECTORY_NAME=logs
LOG_DATE=$(date "+%Y%m%d%H%M%S")

##########################
# input check
##########################
if [ -z $1 ]; then
    echo "No input log name"
    exit 1
else
    LOG_NAME=$1
fi

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

##########################
# make log directory
##########################
cd $MONITORING_HOME
if [ ! -d "$LOG_DIRECTORY_NAME" ]; then
  mkdir $LOG_DIRECTORY_NAME
  echo "make log directory"
fi

##########################
# monitoring start
##########################
cd $MONITORING_HOME/$LOG_DIRECTORY_NAME
nohup docker stats eer --format "{{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}" > "$LOG_NAME-$LOG_DATE.log" 2>&1 &

##########################
# monitoring pid
##########################
cd $MONITORING_HOME/bin
echo $! > docker_monitoring.pid
echo "docker monitoring start"