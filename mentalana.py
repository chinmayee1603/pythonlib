# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mentalanalysis.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sklearn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
class Ui_ThirdWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 546)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.week1 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.week1w)
        self.week1.setGeometry(QtCore.QRect(20, 50, 171, 51))
        self.week1.setObjectName("week1")
        self.week3 = QtWidgets.QPushButton(self.centralwidget)
        self.week3.setGeometry(QtCore.QRect(380, 50, 171, 51))
        self.week3.setObjectName("week3")
        self.week2 = QtWidgets.QPushButton(self.centralwidget)
        self.week2.setGeometry(QtCore.QRect(200, 50, 171, 51))
        self.week2.setObjectName("week2")
        self.week4 = QtWidgets.QPushButton(self.centralwidget)
        self.week4.setGeometry(QtCore.QRect(560, 50, 171, 51))
        self.week4.setObjectName("week4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 161, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.week1.setText(_translate("MainWindow", "WEEK-1"))
        self.week1.clicked.connect(self.week1w)
        self.week3.setText(_translate("MainWindow", "WEEK-3"))
        self.week3.clicked.connect(self.week3w)
        self.week2.setText(_translate("MainWindow", "WEEK-2"))
        self.week2.clicked.connect(self.week2w)
        self.week4.setText(_translate("MainWindow", "WEEK-4"))
        self.week4.clicked.connect(self.week4w)
        self.label.setText(_translate("MainWindow", "Weekly Mood Analysis"))

    def week1w(self):
        df = pd.read_csv('week1.csv')
        sns.countplot(x='emotion', data=df)
        plt.show()
    def week2w(self):
        df = pd.read_csv('week2.csv')
        sns.countplot(x='emotion', data=df)
        plt.show()
    def week3w(self):
        df = pd.read_csv('week3.csv')
        sns.countplot(x='emotion', data=df)
        plt.show()
    def week4w(self):
        df = pd.read_csv('week4.csv')
        sns.countplot(x='emotion', data=df)
        plt.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ThirdWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

