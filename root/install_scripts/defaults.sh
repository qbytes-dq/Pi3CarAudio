#!/bin/bash
# This script to sets default values for Pi3CarAudio
#
clear                           # clear terminal window
#

##-------------------------------------------------
## config.txt updates
##-------------------------------------------------
cp /boot/config.txt /boot/config.txt_defaults

sed -i 's/#dtparam=i2c_arm=on/dtparam=i2c_arm=on #Pi3CarAudio/g' /boot/config.txt
sed -i 's/#dtparam=spi=on/dtparam=spi=on #Pi3CarAudio/g'         /boot/config.txt

echo ""                              >>/boot/config.txt
echo "#---Pi3CarAudio---"            >>/boot/config.txt
echo "# default.sh "                 >>/boot/config.txt
echo "# Performance fixes"           >>/boot/config.txt
echo "gpu_mem=192"                   >>/boot/config.txt
echo "#start_x=1  # not sure"        >>/boot/config.txt

echo ""                              >>/boot/config.txt
echo "# i2c enable"                  >>/boot/config.txt
echo "dtparam=i2c_arm=on"            >>/boot/config.txt
echo "dtparam=spi=on"                >>/boot/config.txt

echo ""                              >>/boot/config.txt
echo "### per my card"               >>/boot/config.txt
echo "#max_usb_current=1"            >>/boot/config.txt
echo "#hdmi_group=2"                 >>/boot/config.txt
echo "#hdmi_mode=1"                  >>/boot/config.txt
echo "#hdmi_mode=87"                 >>/boot/config.txt
echo "#hdmi_cvt 1280 600 60 6 0 0 0" >>/boot/config.txt
sed -i 's/#disable_overscan/disable_overscan #Pi3CarAudio/g' ./config.txt

# http://stackoverflow.com/questions/22891235/how-to-change-screen-resolution-of-raspberry-pi
# https://www.raspberrypi.org/documentation/configuration/config-txt.md
# http://elinux.org/RPiconfig
# http://www.opentechguides.com/how-to/article/raspberry-pi/28/raspi-display-setting.html

