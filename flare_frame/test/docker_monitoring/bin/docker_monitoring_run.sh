#!/bin/sh

MONITORING_HOME=$(cd "$(dirname "$0")" && cd ../;pwd)
LOG_DIRECTORY_NAME=logs
LOGBACK_DIRECTORY_NAME=logs_back
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
  echo "make logs directory"
fi
if [ ! -d "$LOGBACK_DIRECTORY_NAME" ]; then
  mkdir $LOGBACK_DIRECTORY_NAME
  echo "make logs_back directory"
fi

##########################
# backup logs
##########################
cd $MONITORING_HOME
mv ./$LOG_DIRECTORY_NAME/*.log ./$LOGBACK_DIRECTORY_NAME/

##########################
# old process kill
##########################
ps -ef | grep 'docker stats eer' | awk '{print $2}' | while read line; do kill $line; done

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