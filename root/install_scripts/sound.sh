#!/bin/sh
# This script install the software that is required to use USB sound card

clear           # clear terminal window

: ' Comment: Raspbain Jesse does not use the config file like Wheezy

Below line to see avaliable sound cards
$ aplay -l

Below line to adjust mixer volume
$ alsmixer

Below line(s) to test speakers
$ speaker-test -Dplay:front -c2
$ speaker-test -Dplay:front --test sine

'
##-------------------------------------------------
##  OMX Player
##-------------------------------------------------
sudo apt-get -y install omxplayer


##-------------------------------------------------
##  Update alsa.conf to use device 1
##-------------------------------------------------
cp /usr/share/alsa/alsa.conf /usr/share/alsa/alsa.conf_sound

sed -i 's/defaults.ctl.card 0/defaults.ctl.card 1 #0 - Pi3CarAudio.sound/g' /usr/share/alsa/alsa.conf 
sed -i 's/defaults.pmc.card 0/defaults.pmc.card 1 #0 - Pi3CarAudio.sound/g' /usr/share/alsa/alsa.conf 


##-------------------------------------------------
##  update ~/.asoundrc to use device 1
##-------------------------------------------------
cp /home/pi/.asoundrc /home/pi/.asoundrc_sound

sed -i 's/card 0/card 1 #0 - Pi3CarAudio.sound/g' /home/pi/.asoundrc
