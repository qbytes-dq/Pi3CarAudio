
cd /home/pi/Downloads/
rm index.html

wget http://localtimes.info/North_America/United_States/Ohio/

cat index.html | grep "pm</td></tr>" >datetime.txt

#sudo pkill omxplayer >>datetime.txt

omxplayer -o both --no-osd --timeout 10  /home/pi/video1.mp4

#sudo pkill omxplayer >>datetime.txt

echo "done...">>datetime.txt

##exit 0
