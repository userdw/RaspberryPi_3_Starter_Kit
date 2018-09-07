# [ENGLISH] Button Project
In this project we will learn how to use Qt designer in Raspberry Pi 3, at first Make a new project namely ***Widget*** in form creator from Qt designer. After it's done you can see your Main window there, then we will make a simple counter with 3 Button (1 for exit button) and 1 Label for display counter so we need several component below.

## QtGUI Modules
* [QPushButton](http://pyqt.sourceforge.net/Docs/PyQt4/qpushbutton.html)
* [QTextEdit](http://pyqt.sourceforge.net/Docs/PyQt4/qtextedit.html)

<img src="/images/Button1.PNG" height="200">

You can drag & drop the widget that you need from ```widget box``` available on the left side panel

if you press the ```+``` button then counter value will increased by 10, if you press the ```-``` button then counter value will decreased by 10. You can see the value in display label or terminal.

<img src="/images/Button2.PNG" height="200">

if your design has been finish then you must convert it to ***Python*** code using ```pyuic5 -x yourfile.ui -o yourfile.py``` then you can execute with ***Python*** Open your ***lxterminal*** then type ```python3 yourfile.py```

The source code from this project can be found [here](/src)
