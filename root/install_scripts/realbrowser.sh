#!/bin/sh

##--> update key and  repo
wget -qO - http://bintray.com/user/downloadSubjectPublicKey?username=bintray | sudo apt-key add - 
echo "deb http://dl.bintray.com/kusti8/chromium-rpi jessie main" | sudo tee -a /etc/apt/sources.list

## apt-get update
bash ./root/install_scripts/update.sh

#apt-get install -y chromium-browser rpi-youtube
apt-get install -y chromium-browser
apt-get install -y rpi-youtube
