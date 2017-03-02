#!/bin/sh

PIDFILE=/tmp/.d2_automation.pid
NAME=autoaccept.py

if [ -L $BASH_SOURCE ]; then
  DIR=$( dirname "$(readlink -f "$0")" )
else
  DIR=$( dirname "${BASH_SOURCE[0]}" )
fi

SCRIPT=$DIR/$NAME

case "$1" in
  start)
    if [ -e "$PIDFILE" ]; then
      if ( kill -0 $(cat $PIDFILE) 2> /dev/null ); then
        echo "already running..."
        exit 0
      else
        rm -f $PIDFILE
      fi
    fi
    if [ -x "$SCRIPT" ]; then
      "$SCRIPT" > /dev/null &
      PID=$!
      echo $PID > $PIDFILE
      echo "D2 automation started!"
    fi
  ;;
  stop)
    if [ -e "$PIDFILE" ]; then
      kill -9 $(cat $PIDFILE)
      rm $PIDFILE
      echo "stopped"
    else
      echo "stopped (or missing pid :)"
      exit 1
    fi
  ;;
  restart)
    $0 stop; $0 start || exit 1
  ;;
  status)
    if [ -e "$PIDFILE" ]; then
      if ( kill -0 $(cat $PIDFILE) 2> /dev/null ); then
        echo "running..."
      else
        echo "died :("
      fi
    else
      echo "stopped"
    fi
  ;;
  *)
    echo "Usage: ${0} {start|stop|restart|status}"
    exit 2
esac

exit 0
