#!/bin/bash
# This script to install Dev Tools
clear                           # clear terminal window

#==============================
#
# If not run as part of install script (./Pi3CarAudioInstall.sh), you must first run:
#  $ sudo apt-get update
#
#==============================
# Dev tools
#==============================
apt-get -y install filezilla
apt-get -y install dos2unix
apt-get -y install cutecom

#------------------------------
apt-get -y install git
apt-get -y install git-gui

#
# Post install of git
# $ gitconfig --global user.email "your.email@address.here" 
# $ gitconfig --global user.name  "your name here"
#
# or
# nano .gitconfigy 
#
# Usage: 
# $ git gui
# -> clone existing
# - -> source = https://github.com/qbytes-github/Pi3CarAudio
# - -> dest   = /home/pi/Pi3CarAudio     (non existing directory)
# - -> full 
# 
# select files for commint
# Menu
# -> commit
# - ->stage to commit
# - ->commit
#
# Menu (if TAG needed)
# -> Repository
# - -> visualize master history
# - -> right click MASTER comment
# - -> create TAG
#
# Menu
# -> Push
# - -> Include TAGs if you created one
# - -> PUSH
# - -> enter user name "your name here"
# - -> enter password "your password"
#
