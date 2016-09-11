#!/bin/bash
# This script un-installs software that is not needed.
# Raspecially if you’re using Raspian primarily for home automation or electronics.
clear                           # clear terminal window
#


### sudo apt-get remove --purge wolfram-engine penguinspuzzle scratch dillo squeak-vm squeak-plugins-scratch sonic-pi idle idle3 netsurf-gtk netsurf-common

# dillo
# gpicview

# libre-office*
echo "---> removing libre-office*"
apt-get --assume-yes remove --purge libreoffice*

# minecraft-pi
echo "---> removing minecraft-pi"
apt-get --assume-yes remove --purge minecraft-pi

# oracle-java8-jdk
# openjdk-7-jre
# oracle-java7-jdk
# openjdk-8-jre

# penguinspuzzle
echo "---> removing penguinspuzzle"
apt-get --assume-yes remove --purge penguinspuzzle

# scratch
# sonic-pi

# wolfram-engine
echo "---> removing wolfram-engine"
apt-get --assume-yes remove purge wolfram-engine


##----------------------------------------------
##----------------------------------------------
apt-get -y autoremove
apt-get clean

##----------------------------------------------
##----------------------------------------------
##----------------------------------------------
# requires 'sudo su'
# Remove all packages marked rc (thanks @symm)
dpkg --list |grep "^rc" | cut -d " " -f 3 | xargs dpkg --purge 

##----------------------------------------------
##----------------------------------------------
# Remove example files
##----------------------------------------------
rm -rf /home/pi/python_games
rm -rf /opt/vc


# https://project.altservice.com/issues/418

## This site has an excellent scripts....needs review.
# https://blog.samat.org/2015/02/05/slimming-an-existing-raspbian-install/
