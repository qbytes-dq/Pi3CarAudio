#!/bin/bash
# This script installs the GPS on /dev/ttyAMA0
clear				# clear terminal window
#==============================
# update /boot/cmdline.txt
#==============================
cp /boot/cmdline.txt /boot/cmdline.txt_bkup_gpsconfig

# dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p7 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait
#--> remove'console=serial0,115200' and replace with nothing (blank)
sed -i 's/console=serial0,115200//g' /boot/cmdline.txt

echo "##-- gpsconfig.sh values loaded" >>/boot/cmdline.txt

#==============================
# update /boot/config.txt
#==============================
cp /boot/config.txt /boot/config.txt_bkup_gpsconfig
echo ""                               >>/boot/config.txt
echo "##-- gpsconfig.sh added values" >>/boot/config.txt
echo "enable_uart=1"                  >>/boot/config.txt
echo "core_freq=250"                  >>/boot/config.txt
echo "dtoverlay=pi3-miniuart-bt"      >>/boot/config.txt

#==============================
# install GPS software
#==============================
apt-get -y install gpsd gpsd-clients python-gps

# ---------------------
# --- Set defaults  ---
# nano /etc/default/gpsd
# ---------------------
mv /etc/default/gpsd /etc/default/gpsd_bkup_gpsconfig
echo "##-- gpsconfig.sh loaded values"        >/etc/default/gpsd
echo START_DAEMON=\"true\"                   >>/etc/default/gpsd
echo USBAUTO=\"false\"                       >>/etc/default/gpsd
echo DEVICES=\"/dev/ttyAMA0\"                >>/etc/default/gpsd
echo GPSD_OPTIONS=\"-F /var/run/gpsd.socket\">>/etc/default/gpsd

# =============================
### Remove old services
#==============================
# AMA0
systemctl stop    serial-getty@ttyAMA0.service
systemctl disable serial-getty@ttyAMA0.service
# S0
systemctl stop    serial-getty@ttyS0.service
systemctl disable serial-getty@ttyS0.service

#==============================
# New Services
#==============================
### stop/disable new if exists
systemctl stop    gpsd.socket
systemctl disable gpsd.socket

### enable/start new
systemctl enable  gpsd.socket
systemctl start   gpsd.socket

##########################################
### validations
##########################################
# varify  nano /etc/inittab does not contain: TO:23:respawn:/sbin/getty -L ttyAMA0 115200 VT100

##########################################
### Usefull Commands
##########################################
#
# cutecom (from devtools.sh)
# # (9600, )
# apt-get -y install cutecom
#
#
# sudo tail -f /dev/ttyAMA0
# sudo tail -f /dev/ttyS0
#
# ls /dev/ttyUSB*
# ls /dev/ttyAMA*
# ls /dev/ttyS*
#
# gpsmon
#
# cgps
# cgps -s
#
# gpsd /dev/ttyS0   -F /var/run/gpsd.sock(et)?
# gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock(et)?
#
# xgps
#
