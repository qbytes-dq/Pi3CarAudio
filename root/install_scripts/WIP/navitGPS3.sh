####
### Raspian
##  http://wiki.navit-project.org/index.php/Raspberry_Pi
####

# we must be root
#sudo su

##--------------------------------------------------------------------------------
# First of all, we will have to deal with the dependencies:
apt-get -y install subversion imagemagick libdbus-1-dev libdbus-glib-1-dev libfontconfig1-dev libfreetype6-dev libfribidi-dev libimlib2-dev librsvg2-bin libspeechd-dev libxml2-dev ttf-liberation libgtk2.0-dev

# This is for the compiling process:
apt-get -y install gcc g++ cmake make zlib1g-dev libpng12-dev librsvg2-bin

# This is for the SDL graphics (suggested):
apt-get -y install libsdl-image1.2-dev libdevil-dev libglc-dev freeglut3-dev libxmu-dev libfribidi-dev

# This is for the OpenGL support:
apt-get -y install libglc-dev freeglut3-dev libgl1-mesa-dev libfreeimage-dev

# This is QT (note that the QT gui is not maintained currently) :
apt-get -y install libqt4-dev

# This is for GPSd support :
apt-get -y install libgps-dev

# This is espeak, TTS (text to speech)(optional):
apt-get -y install espeak

# If you want to use Garmin maps ( Openstreetmaps are natively supported and are really detailed ) :
#apt-get install libgarmin-dev


##--------------------------------------------------------------------------------
# Ok, 
# now let"s download the latest version of Navit from the repository 
# (starting from your user's folder like /home/pi):
#cd ~/
cd /home/pi/
echo "=================================================="
echo Current directory: $PWD
echo "=================================================="
svn co  svn://svn.code.sf.net/p/navit/code/trunk/navit/ navit

#CMake builds Navit in a separate directory of your choice
# - this means that the directory in which the SVN source was checked out remains untouched.
mkdir navit-build
cd navit-build

#Now the compiling (if you need CSV, keep reading!):
#Note : the freetype library has been updated on raspbian, 
# and this broke cmake's ability to find it. Until this bug is fixed
# ( and cmake is updated to a version > 2.9 ) you will need to add an extra flag to the cmake call :
cmake ~navit -DFREETYPE_INCLUDE_DIRS=/usr/include/freetype2/

#Once the above bug has been fixed, you should be able to use only :
cmake ~/navit

#If you need the CSV support for POIs, you must use:
cmake --enable-map-csv ~/navit

#You are now ready to compile. For a raspberry A, B or B+:
make

#For a raspberry 2:
#make -j4

##--------------------------------------------------------------------------------
#This can take A LOT of time:
#- on a raspberry 2, it takes ~4:30 minutes
#- on a raspberry b+, it takes ~36 minutes
#At the end, you can start Navit (don't forget the configuration! Navit.xml):
cd ~/navit-build/navit/
./navit

#Generating a 3290kms route on the Raspberry pi 2 takes ~ 55s.

##--------------------------------------------------------------------------------
#Adding Support for UART Serial GPS
#connect GPIO on Pi2
# VCC to pin 1, 
# RX to pin 8 
# TX to pin 10 and 
# Ground to pin 6 on GPIO for Pi2
##--------------------------------------------------------------------------------

#Do 
#apt-get install gpsd gpsd-clients python-gps Then sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock test with cpgs -s to autostart gpsd type sudo dpkg-rconfigure gpsd select yes add /dev/ttyAMA0 defaults for everything else.



### Options:
# http://raspberrypi.link-tech.de/doku.php?id=navitnavigation&do=
# http://libresmartphone.com/navigation-system-with-the-ultimate-gps-and-raspberry-pi/
# http://raspberrypi.link-tech.de/doku.php?id=navitnavigation&do=
# https://www.youtube.com/watch?v=QGV4co25WhY&feature=youtu.be
