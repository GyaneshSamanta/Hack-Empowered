# Wheelie - Set Up

1. Download Raspberry Pi OS from this [link](https://www.raspberrypi.com/software/operating-systems/).
2. Flash the image to the SD Card you plan on using with the Pi.
  1. If you're using `Raspberry Pi Imager`
   a. You need to select the Drive (MicroSDHC in this case). 
   b. Choose the OS Version you want to install (Raspbian 32 Bit in this case).
   c. Click on 'Flash'.
  2. If you have the OS image file (.img) you need to install `Balena Etcher` and follow along the same steps as listed in 2.1.
3. Connect the SD Card to your computer again and follow these steps to connect the Pi to your WiFi
  - In the root folder of the SD Card, create a file named `wpa_supplicant.conf` and add the following lines of code to it:
    ``` bash
    country=us
    update_config=1
    ctrl_interface=/var/run/wpa_supplicant

    network={
    scan_ssid=1
    ssid="SSID"
    psk="Password"
    }
  - Create another file named `ssh` without any extensions. These will help us connect with the Raspberry Pi using PuTTY and an Ethernet Cable.
 Make sure that you create these files using Notepad++ or VS Code, using notepad might break the file.  
4. Take the SD Card and insert it in the slot given in the Raspberry Pi. Connect the Ethernet Cable to both the Pi and the Computer and then connect the Pi to power supply.
5. Open PuTTY and connect using `pi@raspberrypi.local` or the IP Address of the Pi if you're able to fetch it from your router and add it in the "Host Name" field. Make sure that you are on Port 22.
6. Login using `pi` as the username and `raspberry` as the password. You can change these later.
7. Run the following set of commands to install and upgrade the libraries required for this project:
  ``` bash
  sudo apt-get upgrade
  pip3 install twilio
  pip3 install RPi.GPIO
  ```
8. Clone this repository using `git clone https://www.github.com/aaishikasb/Hack-Empowered.git`. Then execute `cd Hack-Empowered` to move into the directory.
9. Make changes to the `raspberry-pi-code.py` file to include your own Twilio Credentials, the one's currently in the file are invalid by the time you read this so it won't work. Find your credentials on the [Twilio Console](https://console.twilio.com).
10. Execute the script by using `python3 raspberry-pi-code.py`. 

All set!