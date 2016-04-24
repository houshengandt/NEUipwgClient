# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(469, 210)
        MainWindow.setMinimumSize(QtCore.QSize(469, 210))
        MainWindow.setMaximumSize(QtCore.QSize(469, 210))
        MainWindow.setAcceptDrops(False)
        self.icon = QtGui.QIcon(':/icon.png')
        # self.icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(self.icon)
        MainWindow.setAccessibleName("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(469, 210))
        self.centralwidget.setMaximumSize(QtCore.QSize(469, 210))
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 469, 210))
        self.widget.setMinimumSize(QtCore.QSize(469, 210))
        self.widget.setMaximumSize(QtCore.QSize(469, 210))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label_info = QtWidgets.QLabel(self.widget)
        self.label_info.setEnabled(True)
        self.label_info.setGeometry(QtCore.QRect(290, 0, 181, 211))
        self.label_info.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.label_info.setText("")
        self.label_info.setObjectName("label_info")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 71, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_xywzh = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_xywzh.setGeometry(QtCore.QRect(122, 19, 121, 31))
        self.lineEdit_xywzh.setObjectName("lineEdit_xywzh")
        self.lineEdit_xywmm = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_xywmm.setGeometry(QtCore.QRect(122, 69, 121, 31))
        self.lineEdit_xywmm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_xywmm.setObjectName("lineEdit_xywmm")
        self.pushButton_ljwl = QtWidgets.QPushButton(self.widget)
        self.pushButton_ljwl.setGeometry(QtCore.QRect(70, 150, 75, 31))
        self.pushButton_ljwl.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.pushButton_ljwl.setObjectName("pushButton_ljwl")
        self.pushButton_dklj = QtWidgets.QPushButton(self.widget)
        self.pushButton_dklj.setGeometry(QtCore.QRect(170, 150, 75, 31))
        self.pushButton_dklj.setStyleSheet("background-color: rgb(239, 247, 255);\n"
"background-color: rgb(225, 225, 225);")
        self.pushButton_dklj.setObjectName("pushButton_dklj")
        self.checkBox_zdlj = QtWidgets.QCheckBox(self.widget)
        self.checkBox_zdlj.setGeometry(QtCore.QRect(130, 115, 121, 21))
        self.checkBox_zdlj.setObjectName("checkBox_zdlj")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "校园网客户端"))
        self.label_2.setText(_translate("MainWindow", "校园网账号："))
        self.label_3.setText(_translate("MainWindow", "校园网密码："))
        self.pushButton_ljwl.setText(_translate("MainWindow", "连接网络"))
        self.pushButton_dklj.setText(_translate("MainWindow", "断开网络"))
        self.checkBox_zdlj.setText(_translate("MainWindow", "启动自动连接网络"))
