####
#   Navit 
#   Absolute minimum requirements
#   http://wiki.navit-project.org/index.php/Debian_dependencies
####
apt-get install gcc cmake zlib1g-dev libpng12-dev libgtk2.0-dev librsvg2-bin
#Note: Not all these packages are strictly required (for example, maptool can be built without installing GTK+), 
# but this is the smallest practical set of packages if you want to run Navit.


# ------------------------------------
# Translations for the user interface
apt-get -y install gettext

# ------------------------------------
#GTK+
#Included in minimum requirements

# ------------------------------------
#SDL
apt-get -y install libsdl-image1.2-dev libdevil-dev libglc-dev freeglut3-dev libxmu-dev libfribidi-dev

# ------------------------------------
#OpenGL graphics
apt-get -y install libglc-dev freeglut3-dev libgl1-mesa-dev

# ------------------------------------
#QT
apt-get -y install libqt4-dev
#This package will pull in all the required packages as dependencies.

# ------------------------------------
#gpsd
apt-get -y install libgps-dev
#(optional, but certainly nice to have)

# ------------------------------------
#espeak
apt-get -y install espeak

# ------------------------------------
#(optional)
#speechd
apt-get -y install libspeechd-dev
#(optional, you are better off with using espeak)

# ------------------------------------
#dbus
apt-get -y install libdbus-glib-1-dev
#(optional, you most likely don't need this.)

# ------------------------------------
#python
apt-get -y install python-dev
#(optional, you most likely don't need this.)

# ------------------------------------
#saxon
#apt-get -y install libsaxonb-java
#only required for android
