#!/bin/bash
# This script create CarAudio, displays status in progress
clear				# clear terminal window
# sudo apt-get install dos2unix
# sudo dos2unix ./Pi3CarAudio.sh

#### chmod a+x ./*.sh -R

RED='\033[0;31m'
YELLOW='\033[1;33m'
GRN='\033[0;32m'
NC='\033[0m' # No Color


function print {
echo -e ${GRN}$1${NC}
}

function warn {
echo -e ${YELLOW}$1${NC}
}

function error {
echo -e ${RED}$1${NC}
}

#Black        0;30     Dark Gray     1;30
#Red          0;31     Light Red     1;31
#Green        0;32     Light Green   1;32
#Brown/Orange 0;33     Yellow        1;33
#Blue         0;34     Light Blue    1;34
#Purple       0;35     Light Purple  1;35
#Cyan         0;36     Light Cyan    1;36
#Light Gray   0;37     White         1;37

USER=$(whoami)
print $USER

#print "$EUID" 

if [[ $USER != "root" ]]; then
	# Invalid user
	error "Please run as 'root'"
	error "Example: sudo ./Pi3CarAudioInstall.sh"
	error "Exiting..."
	exit 1
fi #else
	# Run the script
	print "-=-=-Creating CarAudio Pi-=-=-"
	print "     Downloading Scripts"
	#
	print "Current path: $PWD"
	cd ~/
	print "New path: $PWD"

if [[ -d /root/scripts ]]; then
	print "/root/scripts exists!"
else
	mkdir scripts
	print "/root/scripts created."
fi

echo "Script path: $PWD "

#wget -O startup.mp3    http://electronics.qbytesworld.com/file.axd?file=/raspberrypi/scripts/Electrical_Sweep-Sweeper-Startup.mp3

chmod u+x /root/Pi3CarAudio/root/install_scripts/*.sh
#
print "Google DNS"
bash /root/Pi3CarAudio/root/install_scripts/dns.sh

print "Updating Pi 3"
bash /root/Pi3CarAudio/root/install_scripts/update.sh

##-------------------------------------------------
##-------------------------------------------------
# A reboot is required here
##-------------------------------------------------
##-------------------------------------------------
warn "A reboot is needed"
#->reboot

##-------------------------------------------------
print "Installing DEV tools"
bash /root/Pi3CarAudio/root/install_scripts/devtools.sh

##-------------------------------------------------
print "Setting default values"
bash /root/Pi3CarAudio/root/install_scripts/defaults.sh

##-------------------------------------------------
print "Free Space - remove programs not needed"
bash /root/Pi3CarAudio/root/install_scripts/freespace.sh

##-------------------------------------------------
#print "Add Sound"
#bash ./sound.sh

##-------------------------------------------------
print "Real Browswer"
bash /root/Pi3CarAudio/root/install_scripts/realbrowser.sh

##-------------------------------------------------
print "BlueTooth"
#bash ./bluetooth.sh

##-------------------------------------------------
print "GPS Config"
bash /root/Pi3CarAudio/root/install_scripts/gpsconfig.sh

##-------------------------------------------------
##-------------------------------------------------
# A reboot is required here
##-------------------------------------------------
##-------------------------------------------------
warn "A reboot is needed"
#->reboot

##-------------------------------------------------
print "Splash"
bash /root/Pi3CarAudio/root/install_scripts/splash.sh

##-------------------------------------------------
##-------------------------------------------------
# A reboot is required here
##-------------------------------------------------
##-------------------------------------------------
warn "A reboot is needed"
reboot

##-------------------------------------------------
print "DONE!!!"
#fi
