####
##  CMAKE installation
##  https://cmake.org/download/
####

cd ~/

## Download
wget https://cmake.org/files/v3.6/cmake-3.6.1.tar.gz
#wget http://www.cmake.org/files/v2.8/cmake-2.8.3.tar.gz

## unzip
#tar xzf cmake-2.8.3.tar.gz
tar xzf cmake-3.6.1.tar.gz

#cd cmake-2.8.3
cd cmake-3.6.1
./configure --help
./configure --prefix=/opt/cmake
make


#### reboot and run script cmake2.sh
##cd ~/
##cd cmake-3.6.1
###must be root
##make install
##/opt/cmake/bin/cmake -version

