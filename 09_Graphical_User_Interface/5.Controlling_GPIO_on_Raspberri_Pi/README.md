# [ENGLISH] Controllig GPIO on Raspberry Pi
In this project we will make a Graphical User Interface for controlling device conected to raspberry pi. For all information about the widgets you can found [here](http://pyqt.sourceforge.net/Docs/PyQt4/qtgui.html), so we will use several component below:

* [QTextEdit](http://pyqt.sourceforge.net/Docs/PyQt4/qtextedit.html)
* [QPushButton](http://pyqt.sourceforge.net/Docs/PyQt4/qpushbutton.html)
* [QLabel](http://pyqt.sourceforge.net/Docs/PyQt4/qlabel.html)
* [QGroupBox](http://pyqt.sourceforge.net/Docs/PyQt4/qgroupbox.html)

### In this project you will need:
* Raspbery Pi 3 (1),
* Raspberry Pi IO Expansion Shield (1),
* LED Module (1).
* Temperature Sensor (1)
* Digital Push Button (1)

### Assemble the modules following these steps:
1. Plug the Raspberry Pi IO Expansion Shield to the top of  Raspberry Pi 3,
2. Plug the LED Module to the header on the Raspberry Pi IO Expansion Shield labelled **1**,
3. Plug the Digital Push Button Module to the header on the Raspberry Pi IO Expansion Shield labelled **2**,
4. Plug the Temperature Module to the header on the Raspberry Pi IO Expansion Shield labelled **A0**,
5. Run the [Controlling_GPIO_on_Raspberri_Pi](/09_Graphical_User_Interface/5.Controlling_GPIO_on_Raspberri_Pi/src) code in Raspberry Pi 3 with Python.

<img src="/images/Controlling_GPIO1.PNG" height="130">

After your design has complete then press the ```Ctrl+r``` for preview, your preview window will pop up directly.

<img src="/images/Controlling_GPIO.PNG" height="137">

If your design has been finish then you must convert it to ***python*** code using ```pyuic5 -x file.ui -o yourfile.py``` then you can execute it with ```python3 yourfile.py```

The source code from this project can be found [here](/src)

