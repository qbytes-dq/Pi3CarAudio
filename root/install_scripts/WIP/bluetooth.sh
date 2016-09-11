# Setting up Bluetooth on the Raspberry Pi 3
#apt-get update
#apt-get upgrade -y
#apt-get dist-upgrade -y
#rpi-update
#
# Installing the Software PI Bluetooth
apt-get install pi-bluetooth

#  install instead of pi-bluetooth
#sudo apt-get install bluez bluez-firmware

# Your windows manager, aka your desktop
apt-get install blueman

#pi@raspberrypi:~ $ bluetoothctl
#[bluetooth]# help
#Available commands:
#  list                       List available controllers
#  show [ctrl]                Controller information
#  select <ctrl>              Select default controller
#  devices                    List available devices
#  paired-devices             List paired devices
#  power <on/off>             Set controller power
#  pairable <on/off>          Set controller pairable mode
#  discoverable <on/off>      Set controller discoverable mode
#  agent <on/off/capability>  Enable/disable agent with given capability
#  default-agent              Set agent as the default one
#  scan <on/off>              Scan for devices
#  info <dev>                 Device information
#  pair <dev>                 Pair with device
#  trust <dev>                Trust device
#  untrust <dev>              Untrust device
#  block <dev>                Block device
#  unblock <dev>              Unblock device
#  remove <dev>               Remove device
#  connect <dev>              Connect device
#  disconnect <dev>           Disconnect device
#  version                    Display version
#  quit                       Quit program

