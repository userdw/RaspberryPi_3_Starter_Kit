# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Button.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import wiringpi as wpi

LED_MODULE = 1
MIN_PWM=0
MAX_PWM = 100
wpi.wiringPiSetup() # Must be called before calling any I/O function

class Ui_Form(object):
    def __init__(self):
        self.count=0
        #self.MIN_PWM = 0
        #self.MAX_PWM = 100
        # Set PWM on pin LED_MODULE with initial value = MIN_PWM and range = 100
        wpi.softPwmCreate(LED_MODULE, MIN_PWM, MAX_PWM) 

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(330, 200)
        font = QtGui.QFont()
        font.setPointSize(28)
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 30, 161, 51))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.bExit = QtWidgets.QPushButton(Form)
        self.bExit.setGeometry(QtCore.QRect(10, 110, 168, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bExit.setFont(font)
        self.bExit.setObjectName("bExit")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 168, 63))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bMinus = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.bMinus.setFont(font)
        self.bMinus.setObjectName("bMinus")
        self.horizontalLayout.addWidget(self.bMinus)
        self.bMinus.clicked.connect(lambda:self.whichbtn(self.bMinus))
        self.bPlus = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.bPlus.setFont(font)
        self.bPlus.setObjectName("bPlus")
        self.bPlus.clicked.connect(lambda:self.whichbtn(self.bPlus))
        self.horizontalLayout.addWidget(self.bPlus)
        self.layoutWidget.raise_()
        self.label.raise_()
        self.bExit.raise_()

        self.retranslateUi(Form)
        self.bExit.clicked.connect(Form.close)
        wpi.softPwmWrite(LED_MODULE, 0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "CNT"))
        self.bExit.setText(_translate("Form", "EXIT"))
        self.bMinus.setText(_translate("Form", "-"))
        self.bPlus.setText(_translate("Form", "+"))

    def whichbtn(self,b):
        print ("Button "+b.text())
        value=str(b.text())
        #print(value)
        if value == "+" and self.count <100:
          self.count += 10
          wpi.softPwmWrite(LED_MODULE, self.count)
          count=str(self.count)
          print(self.count)
          self.label.setText(count)
        elif value == "-" and self.count > 0:
          self.count -= 10
          wpi.softPwmWrite(LED_MODULE, self.count)
          count=str(self.count)
          print(self.count)
          self.label.setText(count)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

