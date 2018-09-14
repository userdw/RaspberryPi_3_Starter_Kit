# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Controlling_GPIO.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

# Library Declaration
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from time import sleep
import MCP3202, os, wiringpi as wpi

#GPIO's PIN Declaration
LED_MODULE = 1
PUSH_BUTTON=2

#Initial Value Declaration
MIN_PWM=0
MAX_PWM = 100

wpi.wiringPiSetup() 							# Must be called before calling any I/O function
wpi.pinMode(PUSH_BUTTON, wpi.INPUT)
wpi.pullUpDnControl(PUSH_BUTTON, wpi.PUD_DOWN)



class Ui_Form(object):
    def __init__(self):
        self.count=0			# Global variable declaration
        self.pushcount = 0
        # Set PWM on pin LED_MODULE with initial value = MIN_PWM and range = 100
        wpi.softPwmCreate(LED_MODULE, MIN_PWM, MAX_PWM)
		
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(780, 191)	# Main window size
        font = QtGui.QFont()
        font.setPointSize(28)
        Form.setFont(font)
        self.bExit = QtWidgets.QPushButton(Form)
        self.bExit.setGeometry(QtCore.QRect(20, 140, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bExit.setFont(font)
        self.bExit.setObjectName("bExit")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 261, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(200, 30, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.bMinus = QtWidgets.QPushButton(self.groupBox)
        self.bMinus.setGeometry(QtCore.QRect(11, 31, 80, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.bMinus.setFont(font)
        self.bMinus.setObjectName("bMinus")
        self.bMinus.clicked.connect(lambda:self.whichbtn(self.bMinus))
        self.bPlus = QtWidgets.QPushButton(self.groupBox)
        self.bPlus.setGeometry(QtCore.QRect(97, 31, 80, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.bPlus.setFont(font)
        self.bPlus.setObjectName("bPlus")
        self.bPlus.clicked.connect(lambda:self.whichbtn(self.bPlus))
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 30, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(0, 30, 211, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(530, 30, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 30, 211, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Form)
        self.bExit.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
		# Counter
        self.i = 0
        self.j=0
        # Make QTimer
        self.qTimer = QTimer()			# Timer 1 for readTemp() functio
        self.qTimer2=QTimer()			# TImer 2 for readPushButton() function

        # Set interval to 1 s
        self.qTimer.setInterval(1000) 	# 1000 ms = 1 s
        self.qTimer2.setInterval(250) 	# 250 ms = 0.25 s

        # Connect timeout signal to signal handler
        self.qTimer.timeout.connect(self.getSensorValue)
        self.qTimer2.timeout.connect(self.getPushCount)

        # Start timer
        self.qTimer.start()
        self.qTimer2.start()

    def getSensorValue(self):							 
        self.i += 1										# Every timer  has been reset, counter i +1
        self.readTemp()									# Call the readTemp() function
    
    def getPushCount(self):
        self.j += 1										# Every timer  has been reset, counter j +1
        self.readPushButton()							# Call the readTemp() function

    def readTemp(self):
        os.system("clear")
        value1= MCP3202.readADC(0)						# Read ADC value
        voltage = round(float(value1 * 5000 / 4095), 2)
        temperature = (voltage - 500) / 10
        tampil = round(float(temperature), 2)
        self.textEdit.setText('Current Temp : '+'\n'+str(tampil)+'\xb0Celcius')
		
    def readPushButton(self):							# Read Digital Push Button statement
        if wpi.digitalRead(PUSH_BUTTON) == wpi.HIGH:
          self.pushcount += 1							# Count the value
          cnt=str(self.pushcount)
          self.textEdit_2.setText('Button Pressed '+ cnt+' Times')
          print("Button pressed " + str(cnt) + " times")
          while wpi.digitalRead(PUSH_BUTTON) == wpi.HIGH:
            pass
 
    def whichbtn(self,b):								# Read the signal from QPushButton
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
		  
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bExit.setText(_translate("Form", "EXIT"))
        self.groupBox.setTitle(_translate("Form", "LED Control"))
        self.label.setText(_translate("Form", "CNT"))
        self.bMinus.setText(_translate("Form", "-"))
        self.bPlus.setText(_translate("Form", "+"))
        self.groupBox_2.setTitle(_translate("Form", "Temperature"))
        self.groupBox_3.setTitle(_translate("Form", "Button Counter"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

