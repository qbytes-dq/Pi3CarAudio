### BEGIN INIT INFO
# Provides:          noip
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Simple script to start a program at boot
### END INIT INFO

# place in: 
# /home/pi/carscript.sh

##  http://www.cyberciti.biz/faq/linux-unix-formatting-dates-for-display/



espeak "1" 
log=carscript.log
#change /direct/path/to/your/application to the path your application is in.
#cd /direct/path/to/your/application      # example cd /home/pi/myprogram/
cd /home/pi/

echo "Current date: $now"

echo "$log"
NOW=$(date +"%m/%d/%y %r")

echo $NOW>>"$log"
echo $PWD   >>"$log"
echo $USER  >>"$log"
#read abc

cat "$log"
#echo $abc #! /bin/sh


#sudo apt-get update
#sudo apt-get -y install omxplayer
#omxplayer -o hdmi videofile.mp4
#omxplayer -o hdmi myvideo.mp4
#omxplayer  -o hdmi /opt/vc/src/hello_pi/hello_video/test.h264
#omxplayer  -o hdmi /home/pi/Videos/bbb_sunflower_2160p_30fps_normal.mp4
 omxplayer  -o both /home/pi/Videos/small.mp4 
#omxplayer  -o both /home/pi/Videos/small.ogv
#omxplayer  -o hdmi /home/pi/Videos/big_buck_bunny_720p_1mb.mp4

sleep 0.5 # Waits 0.5 second.

espeak "Mr. Q" 


exit 0

