# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Timer.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(570, 138)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(lambda:self.whichbtn(self.pushButton))
        self.pushButton.setCheckable(True)						# Make pushButton Checkable
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 40, 104, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")					# lineEdit for Hour value
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 40, 104, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")				# lineEdit for Minute value
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 40, 104, 70))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")				# lineEdit for Second value
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 50, 20, 41))
        font = QtGui.QFont()
        font.setPointSize(44)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(410, 50, 20, 41))
        font = QtGui.QFont()
        font.setPointSize(44)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(190, 10, 52, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(320, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(450, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Initial value for Counter
        self.timerCnt= self.i=self.j=self.k=0 
 
        # Make QTimer
        self.qTimer = QTimer()			# Timer 1 for readTemp() functio

        # Set interval to 1 s
        self.qTimer.setInterval(1000) 	# 1000 ms = 1 s

        # Connect timeout signal to signal handler
        self.qTimer.timeout.connect(self.timerOn)
        
    def timerOn(self):
        self.timerCnt +=1 
        self.getSecond()
        
    def getSecond(self):
		# Condition 1 
        if (self.i==0 and self.j >0 and self.k ==0):
          self.i =60
          self.j -=1
        # Condition 2
        if (self.i==0 and self.j == 0 and self.k >0):
          self.i =59
          self.j=59
          self.k-=1
        # Condition 3
        if (self.i==0 and self.j > 0 and self.k >0):
          self.i =59
          self.j-=1
        # Condition 4  
        if (self.i==0 and self.j > 0 and self.k > 0):
          self.i =59
          self.k-=1
        # Decrease second value by 1 each timer reset
        self.i -=1	
        self.lineEdit_3.setText(str(self.i))
        self.lineEdit_2.setText(str(self.j))
        self.lineEdit.setText(str(self.k))
        
        if(self.i==0 and self.j ==0 and self.k ==0):
          self.qTimer.stop()					# Stop timer if all of the value has reached zero
          self.timerCnt=0						# Reset the counter value
          self.pushButton.setChecked(False)		# Toogle the pushButton
          self.pushButton.setText("START")  
          self.lineEdit.setText('00')
          self.lineEdit_2.setText('00')
          self.lineEdit_3.setText('00')
          print("Timer STOP")
          
        
    def whichbtn(self,b):						# Read the signal from QPushButton
        print ("Button "+b.text())
        if self.pushButton.isChecked()  :
          self.t_sec=self.lineEdit_3.text() 	# Save the input from lineEdit
          self.i =int(self.t_sec)				# Variable for second 
          self.t_min=self.lineEdit_2.text()
          self.j =int(self.t_min)				# Variable for minute 
          self.t_hour=self.lineEdit.text()
          self.k=int(self.t_hour) 				# Variable for hour 
          print(self.k,self.j,self.i)
          self.pushButton.setText("STOP")
          
          # Check the input value first
          if (self.i==0 and self.j == 0 and self.k == 0):
            self.clickMethod()					# Show message box
            self.pushButton.setChecked(False)
            self.pushButton.setText("START")
          else:
            self.qTimer.start()					# Start timer
        else:
          self.pushButton.setText("START")
          self.qTimer.stop()					# Stop timer
          self.timerCnt=0
          self.lineEdit.setText(str('00'))
          self.lineEdit_2.setText(str('00'))
          self.lineEdit_3.setText(str('00'))
    
    def clickMethod(self):						# Notification window function
      msg=QMessageBox()
      msg.about(msg, "Timer Failed", "Please fill the amount of time first !")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "START"))
        self.lineEdit.setInputMask(_translate("Form", "99"))
        self.lineEdit.setText(_translate("Form", "00"))
        self.lineEdit_2.setInputMask(_translate("Form", "99"))
        self.lineEdit_2.setText(_translate("Form", "00"))
        self.lineEdit_3.setInputMask(_translate("Form", "99"))
        self.lineEdit_3.setText(_translate("Form", "00"))
        self.label.setText(_translate("Form", ":"))
        self.label_2.setText(_translate("Form", ":"))
        self.label_3.setText(_translate("Form", "Hour"))
        self.label_4.setText(_translate("Form", "Minute"))
        self.label_5.setText(_translate("Form", "Second"))

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

