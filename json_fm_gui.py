# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'json_fm.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(827, 522)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 35, 41, 21))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(420, 35, 61, 21))
        self.label_2.setObjectName("label_2")
        self.path = QtWidgets.QTextBrowser(Dialog)
        self.path.setGeometry(QtCore.QRect(50, 30, 256, 31))
        self.path.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.path.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.path.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.path.setWordWrapMode(False)
        self.path.setObjectName("path")
        self.open_file = QtWidgets.QPushButton(Dialog)
        self.open_file.setGeometry(QtCore.QRect(310, 30, 92, 30))
        self.open_file.setAutoDefault(False)
        self.open_file.setObjectName("open_file")
        self.key_word = QtWidgets.QLineEdit(Dialog)
        self.key_word.setGeometry(QtCore.QRect(480, 30, 271, 31))
        self.key_word.setObjectName("key_word")
        self.show_json = QtWidgets.QTextBrowser(Dialog)
        self.show_json.setGeometry(QtCore.QRect(50, 140, 701, 301))
        self.show_json.setObjectName("show_json")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(390, 70, 91, 31))
        self.label_3.setObjectName("label_3")
        self.key_key = QtWidgets.QLineEdit(Dialog)
        self.key_key.setGeometry(QtCore.QRect(480, 70, 271, 31))
        self.key_key.setObjectName("key_key")
        self.sort_json = QtWidgets.QPushButton(Dialog)
        self.sort_json.setGeometry(QtCore.QRect(209, 470, 92, 30))
        self.sort_json.setAutoDefault(False)
        self.sort_json.setObjectName("sort_json")
        self.sort_json.setDisabled(True)
        self.format_json = QtWidgets.QPushButton(Dialog)
        self.format_json.setGeometry(QtCore.QRect(359, 470, 92, 30))
        self.format_json.setAutoDefault(False)
        self.format_json.setObjectName("format_json")
        self.search = QtWidgets.QPushButton(Dialog)
        self.search.setGeometry(QtCore.QRect(509, 470, 92, 30))
        self.search.setAutoDefault(False)
        self.search.setObjectName("search")
        self.clear = QtWidgets.QPushButton(Dialog)
        self.clear.setGeometry(QtCore.QRect(659, 470, 92, 30))
        self.clear.setAutoDefault(False)
        self.clear.setObjectName("clear")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 63, 20))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "JSON解析器"))
        self.label.setText(_translate("Dialog", "路径："))
        self.label_2.setText(_translate("Dialog", "关键字："))
        self.open_file.setText(_translate("Dialog", "打开"))
        self.label_3.setText(_translate("Dialog", "(可选)关键键："))
        self.sort_json.setText(_translate("Dialog", "json排序"))
        self.format_json.setText(_translate("Dialog", "json格式化"))
        self.search.setText(_translate("Dialog", "寻找路径"))
        self.clear.setText(_translate("Dialog", "清空"))
        self.label_4.setText(_translate("Dialog", "展示："))

 
class openFDialog(QWidget):
 
    def __init__(self, filename=None):
        super().__init__()
        self.title = '打开json'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self._filename = filename
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.openFileNameDialog()
 
        self.show()
 
    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, self.title, "","JSON Files (*.json);;All files (*)", options=options)
        if fileName:
            self.fileName = fileName
        elif self._filename == '' or self._filename == None:
            pop = popupWindow("未选择文件")

class popupWindow(QWidget):
 
    def __init__(self, message):
        super().__init__()
        self.title = '提示'
        self.left = 410
        self.top = 210
        self.width = 320
        self.height = 200
        self._message = message
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        buttonReply = QMessageBox.question(self, '提示', self._message, QMessageBox.Yes)
 
        self.show()

