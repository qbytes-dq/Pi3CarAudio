#!/bin/sh
echo "Latest and Greatest"
apt-get update
apt-get upgrade -y
apt-get dist-upgrade -y
rpi-update

