sudo apt-get update sudo apt-get install navit
# ls -l /usr/share/navit ls -l /etc/navit ls -l /usr/bin/ | grep navit 
#center.txt mg: 0x13a00a 0x5d6adf
 
cp /etc/navit/navit.xml ~/.navit/ <config 
xmlns:xi="http://www.w3.org/2001/XInclude" language="en_US">
=============================================================


wget -O muenchen.osm "http://api.openstreetmap.org/api/0.6/map?bbox=11.54,48.14,11.543,48.145"

Fetch box 
Top Right:  
84,  -10.4
 
Bottom left:  
6.5,  -178.1
 
wget -O map1.osm http://www.openstreetmap.org/api/0.5/map?bbox=-122.2,47.5,-122,47.7
wget -O map2.osm http://www.openstreetmap.org/api/0.5/map?bbox=-122.4,47.5,-122.2,47.7
wget -O map3.osm http://www.openstreetmap.org/api/0.5/map?bbox=-122.4,47.3,-122.2,47.5
wget -O map4.osm http://www.openstreetmap.org/api/0.5/map?bbox=-122.2,47.3,-122,47.5


--->DAQ
wget -O map1.osm http://www.openstreetmap.org/api/0.5/map?bbox=84,-10.4,6.5,-178.1
 

http://maps6.navit-project.org/
wget http://maps.navit-project.org/planet.bin ## 6+ GB

