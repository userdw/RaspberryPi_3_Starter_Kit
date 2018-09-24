# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pixmap.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 621)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.menuView.setFont(font)
        self.menuView.setObjectName("menuView")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.actionOpen.setFont(font)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        
        self.actionZoom_In_25 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.actionZoom_In_25.setFont(font)
        self.actionZoom_In_25.setObjectName("actionZoom_In_25")
        
        self.actionZoom_Out_25 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.actionZoom_Out_25.setFont(font)
        self.actionZoom_Out_25.setObjectName("actionZoom_Out_25")
        
        self.actionNormal_Size = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.actionNormal_Size.setFont(font)
        self.actionNormal_Size.setObjectName("actionNormal_Size")
        
        self.actionFit_to_Window = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.actionFit_to_Window.setFont(font)
        self.actionFit_to_Window.setObjectName("actionFit_to_Window")
        
        # Setup Label using QLabel for QPixmap
        self.imageLabel = QLabel()
        self.imageLabel.setBackgroundRole(QtGui.QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)
        # Setup Scroll Area for image viewer
        MainWindow.scrollArea = QScrollArea()
        MainWindow.scrollArea.setBackgroundRole(QPalette.Dark)
        MainWindow.scrollArea.setWidget(self.imageLabel)
        MainWindow.setCentralWidget(MainWindow.scrollArea)
		
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Routine for Create Menus and Actions bar
        self.createActions()
        self.createMenus()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionZoom_In_25.setText(_translate("MainWindow", "Zoom In (25%)     Ctrl ++"))
        self.actionZoom_Out_25.setText(_translate("MainWindow", "Zoom Out (25%)  Ctrl +-"))
        self.actionNormal_Size.setText(_translate("MainWindow", "Normal Size"))
        self.actionFit_to_Window.setText(_translate("MainWindow", "Fit to Window"))
    
    # updateActions routine declare a function to update state condition for ZoomIn/Out action
    def updateActions(self):
        self.actionZoom_In_25.setEnabled(not self.actionFit_to_Window.isChecked())
        self.actionZoom_Out_25.setEnabled(not self.actionFit_to_Window.isChecked())
        self.actionNormal_Size.setEnabled(not self.actionFit_to_Window.isChecked())
        
    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

        self.adjustScrollBar(MainWindow.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(MainWindow.scrollArea.verticalScrollBar(), factor)

        self.actionZoom_In_25.setEnabled(self.scaleFactor < 3.0)	# Maximum ZoomIn factor
        self.actionZoom_Out_25.setEnabled(self.scaleFactor > 0.333)	# Maximum ZoomOut factor
    
    def adjustScrollBar(self, scrollBar, factor):					# Adjust Scrollbar factor
        scrollBar.setValue(int(factor * scrollBar.value()
          + ((factor - 1) * scrollBar.pageStep()/2)))
    
    # This subroutine for call a fileDialog function
    def open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        # Setup filename extension for an image file only ".jpg" and ".png" are allowed
        # to read.
        fileName, _ = QFileDialog.getOpenFileName(MainWindow,"QFileDialog.getOpenFileName()", " ",
        "All Files (*);;Image Files (*.jpg);;Image Files (*.png)", options=options)
        if fileName:
            image = QtGui.QImage(fileName)
            if image.isNull():
                # Exception when user load a wrong file
                QMessageBox.information(MainWindow, "Open Failed",
                        "Cannot load %s." % fileName,QMessageBox.Ok,QMessageBox.NoButton)
                return
			# Setup QPixmap for display an image file
            self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
            self.scaleFactor = 1.0										# Normal scale factor
            self.actionFit_to_Window.setEnabled(True)
            self.updateActions()										# UpdateAction routine
            
            if not self.actionFit_to_Window.isChecked():
                self.imageLabel.adjustSize()
    
    def createMenus(self):
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionZoom_In_25)
        self.menuView.addAction(self.actionZoom_Out_25)        
        self.menuView.addAction(self.actionNormal_Size)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFit_to_Window)        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAbout)
        
    def createActions(self):
        self.actionOpen =QAction("Open", MainWindow)
        self.actionOpen.setShortcut('Ctrl+o')					# Shortcut key for open a file
        self.actionOpen.triggered.connect(self.open)
        
        self.actionExit =QAction("Close", MainWindow)
        self.actionExit.setShortcut('Ctrl+Q')					# Shortcut key for close window
        self.actionExit.triggered.connect(MainWindow.close)
        
        self.actionZoom_In_25 =QAction("Zoom In", MainWindow)
        self.actionZoom_In_25.setShortcut("Ctrl+]")				# Shortcut key for Zoom In
        self.actionZoom_In_25.triggered.connect(self.zoomIn)
        self.actionZoom_In_25.setEnabled(False)     

        self.actionZoom_Out_25 =QAction("Zoom Out", MainWindow)
        self.actionZoom_Out_25.setShortcut('Ctrl+[')			# Shortcut key for Zoom Out
        self.actionZoom_Out_25.triggered.connect(self.zoomOut)        
        self.actionZoom_Out_25.setEnabled(False)
        

        self.actionNormal_Size =QAction("Normal Size", MainWindow)	# Shortcut key for Normal Size
        self.actionNormal_Size.setShortcut('Ctrl+n')
        self.actionNormal_Size.triggered.connect(self.normalSize)          
        self.actionNormal_Size.setEnabled(False)
        
        self.actionFit_to_Window =QAction("Fit Window", MainWindow)	# Shortcut key for fitToWindow
        self.actionFit_to_Window.setShortcut('Ctrl+f')
        self.actionFit_to_Window.triggered.connect(self.fitToWindow)
        self.actionFit_to_Window.setEnabled(False)
        self.actionFit_to_Window.setCheckable(True)
        
        self.menuAbout =QAction("About", MainWindow)
        self.menuAbout.triggered.connect(self.about)
        
        
    # Below are functions which control the image size  
    def zoomIn(self):
        self.scaleImage(1.5)
        print("Zoom in : ", round(self.scaleFactor,2),"X")
        
    def zoomOut(self):
        self.scaleImage(0.8)
        print("Zoom Out : ", round(self.scaleFactor,2),"X")        
    
    def normalSize(self):
		# When normal size function has been called then scrollarea must be disabled
        MainWindow.scrollArea.setWidgetResizable(False)
        self.imageLabel.adjustSize()
        self.scaleFactor = 1.0
        print("Normal size : ", round(self.scaleFactor,2),"X")
        
    def fitToWindow(self):
		# When fitToWindow function has been called then all of zoom function
		# and normalSize function will be disabled
        fitToWindow = self.actionFit_to_Window.isChecked()
        MainWindow.scrollArea.setWidgetResizable(True)
        if not fitToWindow:
            self.normalSize()
        self.updateActions()
        
    def about(self):
        QMessageBox.about(MainWindow, "About Image Viewer",
                "<p>The <b>Image Viewer</b> example shows how to combine "
                "QLabel and QScrollArea to display an image. QLabel is "
                "typically used for displaying text, but it can also display "
                "an image. QScrollArea provides a scrolling view around "
                "another widget. If the child widget exceeds the size of the "
                "frame, QScrollArea automatically provides scroll bars.</p>"
                "<p>The example demonstrates how QLabel's ability to scale "
                "its contents (QLabel.scaledContents), and QScrollArea's "
                "ability to automatically resize its contents "
                "(QScrollArea.widgetResizable), can be used to implement "
                "zooming and scaling features.</p>"
                "<p>In addition the example shows how to use QPainter to "
                "print an image.</p>")
                
                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

