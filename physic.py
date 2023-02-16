# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'physicanalysis.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SecondWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(600, 522)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 40, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 80, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 130, 111, 16))
        self.label_3.setObjectName("label_3")
        self.height = QtWidgets.QTextEdit(self.centralwidget)
        self.height.setGeometry(QtCore.QRect(200, 70, 171, 31))
        self.height.setObjectName("height")
        self.weight = QtWidgets.QTextEdit(self.centralwidget)
        self.weight.setGeometry(QtCore.QRect(200, 120, 171, 31))
        self.weight.setObjectName("weight")
        self.calbmi = QtWidgets.QPushButton(self.centralwidget)
        self.calbmi.setGeometry(QtCore.QRect(200, 190, 111, 31))
        self.calbmi.setObjectName("calbmi")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 270, 111, 16))
        self.label_4.setObjectName("label_4")
        self.bmi = QtWidgets.QTextEdit(self.centralwidget)
        self.bmi.setGeometry(QtCore.QRect(200, 260, 171, 31))
        self.bmi.setObjectName("bmi")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label.setText(_translate("mainWindow", "BMI"))
        self.label_2.setText(_translate("mainWindow", "Enter Your Height:"))
        self.label_3.setText(_translate("mainWindow", "Enter Your Weight:"))
        self.calbmi.setText(_translate("mainWindow", "Calculate BMI"))
        self.label_4.setText(_translate("mainWindow", "Your BMI :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

