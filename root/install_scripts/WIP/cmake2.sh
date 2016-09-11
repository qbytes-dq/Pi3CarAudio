####
##  CMAKE installation
##  https://cmake.org/download/
## -----------------------------> Post reboot
####

cd  ~/
#cd /home/pi/scripts
cd /home/pi/
cd cmake-3.6.1

#must have been root
make install

## Update path (temp update)
PATH=/opt/cmake/bin:$PATH

## Update path (perm update)
echo ""  >> ~/.profile
echo "PATH=/opt/cmake/bin:\$PATH" >> /home/pi/.profile

cmake -version

