# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\TabletDMI.ui'
#
# Created: Tue Nov 12 11:23:43 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(596, 277)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("TabletDMI.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 201, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 81, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 50, 201, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 80, 201, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 81, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 81, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 110, 201, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 140, 391, 20))
        self.lineEdit_5.setText(_fromUtf8(""))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 81, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 81, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 170, 391, 20))
        self.lineEdit_6.setText(_fromUtf8(""))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 20, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 50, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 80, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 110, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(500, 140, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 170, 75, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(100, 200, 75, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(200, 200, 75, 23))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(300, 200, 75, 23))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(400, 200, 75, 23))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 596, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "TabletDMI", None))
        self.label.setText(_translate("MainWindow", "Manufacture", None))
        self.label_2.setText(_translate("MainWindow", "ProductName", None))
        self.label_3.setText(_translate("MainWindow", "Version(P/N)", None))
        self.label_4.setText(_translate("MainWindow", "SN/PPID", None))
        self.label_5.setText(_translate("MainWindow", "UUID", None))
        self.label_6.setText(_translate("MainWindow", "OEM String", None))
        self.pushButton.setText(_translate("MainWindow", "Modify", None))
        self.pushButton_2.setText(_translate("MainWindow", "Modify", None))
        self.pushButton_3.setText(_translate("MainWindow", "Modify", None))
        self.pushButton_4.setText(_translate("MainWindow", "Modify", None))
        self.pushButton_5.setText(_translate("MainWindow", "Modify", None))
        self.pushButton_6.setText(_translate("MainWindow", "Modify", None))
        self.pushButton_7.setToolTip(_translate("MainWindow", "Read All DMI info", None))
        self.pushButton_7.setText(_translate("MainWindow", "Read DMI", None))
        self.pushButton_8.setToolTip(_translate("MainWindow", "Write all DMI info input in edit boxes", None))
        self.pushButton_8.setText(_translate("MainWindow", "Write DMI", None))
        self.pushButton_9.setToolTip(_translate("MainWindow", "Reset Tablet from RockUSB mode", None))
        self.pushButton_9.setText(_translate("MainWindow", "Reset", None))
        self.pushButton_10.setToolTip(_translate("MainWindow", "Clean all of above editboxes", None))
        self.pushButton_10.setText(_translate("MainWindow", "Clean", None))

