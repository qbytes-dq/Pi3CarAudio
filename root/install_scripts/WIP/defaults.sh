###defaults.sh

##==========================================
/etc/default/locale
#  File generated by update-locale
LANG=en_US.UTF-8

##==========================================
/etc/default/keyboard
# KEYBOARD CONFIGURATION FILE

# Consult the keyboard(5) manual page.

XKBMODEL="pc101"
XKBLAYOUT="us,de,fr,ua,ru"
XKBVARIANT=""
XKBOPTIONS="grp:alt_shift_toggle"

BACKSPACE="guess"

##==========================================
##$ setxkbmap -model pc105 -layout us -variant altgr-intl

##==========================================
dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait logo.nologo quiet --add rw init-/bin/sh


####   cat config.txt
dtparam=audio=on
gpu_mem=128
##==========================================

##==========================================

##==========================================

##==========================================

##==========================================
# find all files modified in last 24 hours
find / -mtime -1 -print > ~/24h.txt

##==========================================
# find all files modified in last 60 minutes
sudo find / -amin -60 -print > ~/60m.txt
sudo find / -type f -amin -15
