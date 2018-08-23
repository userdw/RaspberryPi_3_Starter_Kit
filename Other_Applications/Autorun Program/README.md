# [ENGLISH] Autorun Program on Raspberry Pi
This is the simple way to make your program/script run automatically after GUI started on Raspberry Pi. Follow the instructions below :

1. Open lxterminal then type ```sudo nano /home/pi/.config/lxsession/LXDE-pi/autostart```
2. Add the command ```@lxterminal``` in the last line of configuration file. This configuration will make the lxterminal automatically open after GUI environment started


<img src="/images/lxterminal.PNG" height="400">

3. Save the file with press ```Ctrl``` + ```x``` then ```y``` followed up by ```Enter```
4. Open the bashrc file, type  ```sudo nano /home/pi/.bashrc```
5. Add the command for your script i.e sudo python3 ```sudo python /home/pi/Desktop/tes.py```
6. Save the file with press ```Ctrl``` + ```x``` then ```y``` followed up by ```Enter```
7. Then type ```sudo reboot``` in the lxterminal, then your script automatically started after reboot your Raspberry Pi 
