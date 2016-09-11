sudo apt-get update
sudo apt-get install navit
# ls -l /usr/share/navit
# ls -l /etc/navit
# ls -l /usr/bin/ | grep navit

#center.txt
#mg: 0x13a00a 0x5d6adf
 
cp /etc/navit/navit.xml ~/.navit/

<config xmlns:xi="http://www.w3.org/2001/XInclude" language="en_US">


=============================================================
http://www.dynacont.net/documentation/linux/Useful_SystemD_commands/
=============================================================

startup script
http://askubuntu.com/questions/9382/how-can-i-configure-a-service-to-run-at-startup
http://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up
http://www.stuffaboutcode.com/2012/06/raspberry-pi-run-program-at-start-up.html
https://www.raspberrypi.org/documentation/linux/usage/rc-local.md

=============================================================
shutdown script
http://raspberrypi.stackexchange.com/questions/15571/how-to-add-start-up-and-shutdown-script
https://www.element14.com/community/docs/DOC-78055/l/adding-a-shutdown-button-to-the-raspberry-pi-b

=============================================================

https://www.youtube.com/user/RaspberryPiBeginners/videos
-------------------------------------------------------------

https://www.youtube.com/watch?v=IX4f3BWOwAc
https://www.youtube.com/watch?v=IX4f3BWOwAc

http://goo.gl/g05pzE
https://dl.dropboxusercontent.com/u/106074492/video.mp4

sudo apt-get -y install omxplayer

sudo wget -O asplashscreen http://goo.gl/sqDMT3

sudo nano asplashscreen
--> change .mov to .mp4

sudo nano /boot/cmdline.txt
--> add 'quiet' to the end

sudo chmod a+x /etc/init.d/asplashscreen

sudo insserv /etc/init.d/asplashscreen
--> ensures script is added to boot sequence.

sudo nano /etc/rc.local
--> add 'clear' prior to 'exit 0'

======================================================
VNC
https://www.youtube.com/watch?v=c5QCoh8S0N4

======================================================
power supply
https://www.youtube.com/watch?v=9rPUODcKWIM
https://www.youtube.com/watch?v=lM_fUPE9Lm8
https://www.youtube.com/watch?annotation_id=annotation_71358&feature=iv&src_vid=lM_fUPE9Lm8&v=w4vSTq2WhN8

======================================================
XBMC Media Centre
https://www.youtube.com/watch?v=kNSPW1VWlJk


