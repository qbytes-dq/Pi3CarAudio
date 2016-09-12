#!/bin/bash
# This script installs software that is required for GPIO and python.

clear                           # clear terminal window
#

##-------------------------------------------------
## Raspbian distro already has the i2c driver installed by the are disabled.
## TO enable it, comment out the line by putting a # in front.
##-------------------------------------------------
cp /etc/modprobe.d/raspi-blacklist.conf /etc/modprobe.d/raspi-blacklist.conf_gpio

sed -i 's/blacklist spi-bcm2708/blacklist spi-bcm2708 #Pi3CarAudio/g' /etc/modprobe.d/raspi-blacklist.conf
sed -i 's/blacklist i2c-bcm2708/blacklist i2c-bcm2708 #Pi3CarAudio/g' /etc/modprobe.d/raspi-blacklist.conf

echo ""                         >>/etc/modprobe.d/raspi-blacklist.conf
echo "#---Pi3CarAudio.gpio---"       >>/etc/modprobe.d/raspi-blacklist.conf

##-------------------------------------------------
## Add i2c-dev  to  /etc/modules  (remove it and force an add of it back in)
##-------------------------------------------------
cp /etc/modules /etc/modules_gpio
sed -i 's/i2c-dev/#i2c-dev #Pi3CarAudio/g' /etc/modules

echo ""                         >>/etc/modules
echo "#---Pi3CarAudio.gpio---"       >>/etc/modules
echo "i2c-dev"                  >>/etc/modules

##-------------------------------------------------
## Required programs
##-------------------------------------------------
apt-get -y install  i2c-tools
apt-get -y install  python-smbus

#apt-get update
bash ./root/install_scripts/update.sh

adduser pi i2c

#-----------------------
## a reboot is required.
#-----------------------
#apt-get -y install python-rpi.gpio python3-rpi.gpio


## TOOLS
#
#  ls -l /dev/ | grep i2c
#
#  i2cdetect -l
#--------older versions
# sudo i2cdetect -y 0 
#
#--------new version (my RPi 3 is this)
# sudo i2cdetect -y 1
#

## http://skpang.co.uk/blog/archives/575
