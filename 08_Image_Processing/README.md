# [ENGLISH] Image Processing
Commonly found microcontrollers can't handle any application that involves image processing as one of its features, because the available resources aren't enough. Usually, the last resort is to utilize computer/laptop for that matter.

As you can see, the look of the robot is somewhat terrible and expensive at the same time. Now we can actually replace the laptop with Raspberry Pi 3, therefore the price for building one would be far cheaper and not to mention that the appearance would be somewhat better. In this part we will try to do some image processing stuffs on Raspberry Pi 3 with Python 3 and OpenCV.

## OpenCV Installation
Before we get started, we need to install OpenCV on our Raspberry Pi 3. The installation can be done by following the steps below:
* Type and run the commands below on your terminal:
```
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk2.0-dev libgtk-3-dev
sudo apt-get install libcanberra-gtk*
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install python2.7-dev python3-dev
cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
unzip opencv.zip
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
unzip opencv_contrib.zip
cd ~/opencv-3.3.0/
mkdir build
cd build
```
* Type and run the command below:
```
cmake -D CMAKE_BUILD_TYPE=RELEASE \
  -D CMAKE_INSTALL_PREFIX=/usr/local \
  -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.0/modules \
  -D ENABLE_NEON=ON \
  -D ENABLE_VFPV3=ON \
  -D BUILD_TESTS=OFF \
  -D INSTALL_PYTHON_EXAMPLES=OFF \
  -D BUILD_EXAMPLES=OFF ..
```
* Open ```/etc/dphys-swapfile``` then edit ```CONF_SWAPSIZE=100``` to ```CONF_SWAPSIZE=1024```.
* Type and run the command below:
```
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
make -j4
sudo make install
sudo ldconfig
```
* Open ```/etc/dphys-swapfile``` then edit ```CONF_SWAPSIZE=1024``` to ```CONF_SWAPSIZE=100```.
* Type and run the command below:
```
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
```
* Check OpenCV installation by typing commands below on Python 3:
```
import cv2
print(cv2.__version__)
```
If there are no errors prompted, then we've been successfully installed OpenCV on our Raspberry Pi 3.

### In this project you will need:
* Raspbery Pi 3 (1),
* Raspberry Pi IO Expansion Shield (1),
* LED Module (1).

<img src="/images/blinking and fading LED.png" height="400">

### Assemble the modules following these steps:
1. Plug the Raspberry Pi IO Expansion Shield to the top of  Raspberry Pi 3,
2. Plug the LED Module to the header on the Raspberry Pi IO Expansion Shield labelled **9**,
3. Run the [Blinking_and_Fading_a_LED](/01_Blinking_and_Fading_a_LED/Blinking_and_Fading_a_LED.py) code in Raspberry Pi 3 with Python. 

If there are no mistakes, the LED Module should start blinking then increase and fade in its brightness.

# [BAHASA INDONESIA] Image Processing
Under construction
