####
##  Navit
##  http://wiki.navit-project.org/index.php/Linux_development
####

## Getting Navit from the GIT repository
cd ~/
git clone https://github.com/navit-gps/navit.git

## Compiling navit
mkdir navit-build
cd navit-build
/opt/cmake/bin/cmake ~/navit
make

#rm -r ~/navit-build/*
#/opt/cmake/bin/cmake ~/navit

## Run navit
cd ~/navit-build/navit/
./navit
