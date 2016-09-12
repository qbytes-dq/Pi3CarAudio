#!/bin/sh
## 

### http://www.raspberry-projects.com/pi/pi-operating-systems/raspbian/custom-boot-up-screen
# did not do next 2 lines yet
# add vt.global_cursor_default=0  ### mine not blinking
# add dwc_otg.lpm_enable=0        ### not sure what it does
# loglevel=3                      ### display only non critical kernel log messages

#==============================
# edit /boot/cmdline.txt
#==============================
cp /boot/cmdline.txt /boot/cmdline.txt_bkup_splash

echo ""                             >>/boot/cmdline.txt
echo "##-- splash.sh values added/updated" >>/boot/cmdline.txt

#--> add 'nologo' and 'quiet' to the end cmdline.txt
sed -i 's/rootwait/rootwait logo.nologo quiet/g' /boot/cmdline.txt

#--> replace 'console=tty1' with 'console=tty3'
sed -i 's/console=tty1/console-tty3/g' /boot/cmdline.txt

#==============================
# edit /boot/config.txt
#==============================
## http://blog.fraggod.net/2015/11/28/raspberry-pi-early-boot-splash-logo-screen.html
cp /boot/config.txt /boot/config.txt_bkup_splasy

echo ""                              >>/boot/cmdline.txt
echo "##-- splash.sh values added/updated" >>/boot/cmdline.txt

echo "disable_splash=1 #Pi3CarAudio"  >>/boot/config.txt
echo "avoid_warnings=1 #Pi3CarAudio"  >>/boot/config.txt


#==============================
#--> copy script to /etc/init.d
#==============================
cp ./etc/init.d/splashscreen.sh /etc/init.d/splashscreen.sh
chmod a+x /etc/init.d/splashscreen.sh

#==============================
#--> copy png and mp4 to /etc/
#==============================
cp ./etc/distracted/distracted4.png /etc/distracted.png
cp ./etc/models/Mercedes-Benz2.mp4  /etc/model.mp4

#==============================
## make script auto start
#==============================
insserv /etc/init.d/splashscreen.sh -r -f  ## just in case it exists already
insserv /etc/init.d/splashscreen.sh

#==============================
# edit /etc/rc.local
#==============================
# --> ensures script is added to boot 
#sequence. sudo nano /etc/rc.local
cp /etc/rc.local /etc/rc.local_bkup

#--> add 'clear' prior to 'exit 0'
sed -i 's/'^exit'/clear #Pi3CarAudio \
exit/g' /etc/rc.local

#==============================
#--> install needed applications
#==============================
apt-get -y install fbi
apt-get -y install omxplayer

#==============================
# apply and test
#==============================
reboot

# # wget -O asplashscreen http://goo.gl/sqDMT3 sudo
