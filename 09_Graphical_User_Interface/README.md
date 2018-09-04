# [ENGLISH] Project 9: Graphical User Interface
Raspberry Pi 3 is a mini computer, therefore most of things that can be done on normal computer can be done as well on Raspberry Pi 3. Graphical User Interface programming, or GUI programming for short, is one of them. With Raspberry Pi 3 we can make sophisticated GUI design with less effort when compared to microcontroller. In this project we will try to do some GUI design and programming on Raspberry Pi 3 using Python and Qt.

## Installation
Before we get started, we need to install Qt on our Raspberry Pi 3. The installation can be done by following the steps below:
* Type and run the commands below on your terminal to install all the required tools and packages for Qt on Raspberry Pi 3:
```
sudo apt-get install python3-pyqt5
sudo apt-get install qttools5-dev-tools
sudo apt-get install qtcreator pyqt5-dev-tools
```
* We will use Qt Designer to design our GUI. The installation has been done in the previous step, and can be found in ```/usr/lib/arm-linux-gnueabihf/qt5/bin/designer```. To make it easier for us to open it, we can make a desktop shortcut for it. Follow the steps below to make the shortcut:
    * Make a new file on desktop without any extension. Give it an easy to remember name, for example ```Qt Designer```.
    * Insert the code below to the file created before:
```
[Desktop Entry]
Name=Qt Designer
Comment=Qt Designer
Exec=sudo /usr/lib/arm-linux-gnueabihf/qt5/bin/designer
Type=Application
Encoding=UTF-8
Terminal=false
Categories=None;
```
* You can open Qt Designer by double-clicking the file.

<img src="/images/Qt.png" height="400">

After design your own ui(user interface) then the output file from Qt Designer is some file with ```.ui``` extension, this file purely design code form Qt Designer. We must convert the file into Python code with ```.py``` extension first,  then we can add some code and execute it with Python we can open the **lxterminal** then type ```pyuic5 -x file.ui -o file.py```, **-x** for execute **-o** for output so make sure you're on the right directory.

Note : ```pyuic5``` the version depends on your installation, you can check the manual for ```pyuic``` with type in **lxterminal** ```man pyuic5``` (if you'r using version 5 pyuic)

<img src="/images/manpyuic5.PNG" height="400">

## The topics which will be included in this project are:
* [Button](/09_Graphical_User_Interface/Button/)
* [Input Widgets]
* [Display Widgets].
* [Timer]
* [Controlling Raspberry Pi 3's I/O through GUI]
