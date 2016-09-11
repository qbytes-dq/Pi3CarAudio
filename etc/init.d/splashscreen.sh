#!/bin/sh
### BEGIN INIT INFO
# Provides:          custom splash and video
# Required-Start:
# Required-Stop:
# Should-Start:
# Default-Start:     S
# Default-Stop:      0 1 6
# X-Interactive:
# Short-Description: Simple script to start a program at boot
### END INIT INFO

# place in:
#--->>>???? /home/pi/carscript.sh

##  http://www.cyberciti.biz/faq/linux-unix-formatting-dates-for-display/

#sudo apt-get update
#sudo apt-get -y install omxplayer

#PATH=/sbin:/bin
PATH=/sbin:/bin:$PATH

cd /home/pi/
log=carscript.log

NOW=$(date +"%m/%d/%y %r")
echo "Now   :$NOW" >>"$log"
echo "User  :$USER">>"$log"
echo "PWD   :$PWD" >>"$log"
echo "Param1: $1"  >>"$log"
echo "Param2: $2"  >>"$log"
echo "Param3: $3"  >>"$log"

#---------------------------------------------------------------
do_start () {

    killall -9 fbi
    killall -9 omxplayer
    killall -9 omxplayer.bin

    /usr/bin/fbi -T 1 -t 5 -l --fitwidth -noverbose /etc/distracted.png
#    sleep 5

#    omxplayer -o both --no-osd --win "0,0,1280,600" /etc/model.mp4 &
     omxplayer -o both --no-osd --aspect-mode stretch /etc/model.mp4 &
    #sleep 0.5 # Waits 1/2 second.

    ps -ef | grep fbi >>"$log"
    killall -9 fbi
}

case "$1" in
  start|"")
	echo "Start"
	espeak "Start"
        do_start
        ;;
  restart|reload|force-reload)
        echo "Error: argument '$1' not supported" >&2
	espeak "Restart"
        exit 3
        ;;
  stop|status)
	echo "Stop|Status"
	espeak "Stop"
        # No-op
        ;;
  *)
        echo "Usage: $0 start|stop" >&2
	espeak "Unknown"
        exit 3
        ;;
esac

:

exit 0

