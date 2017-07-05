#!/usr/bin/python 
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from json_fm_gui import Ui_Dialog, openFileDialog, popupWindow
import json
 
class json_ui_dialog(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        # Connect "add" button with a custom function (addInputTextToListbox)
        #self.addBtn.clicked.connect(self.addInputTextToListbox)
        self.clear.clicked.connect(self.clear_all_text)
        self.open_file.clicked.connect(self.openFile)
        self.format_json.clicked.connect(self.formatJson)
        self.search.clicked.connect(self.searchJson)

    def clear_all_text(self):
        self.key_key.setText('')
        self.key_word.setText('')
        self.show_json.setText('')
        self.path.setText('')

    def searchJson(self):
        if self.path.toPlainText() == '':
            pop = popupWindow("未选择文件")
            self.openFile()
            return 1
        elif self.key_word.toPlainText() == '':
            pop = popupWindow("未设定关键字")
            return 1
        output = list()
        jsonH = jsonHandler()
        jsonH.getJson(self.path.toPlainText())
        jsonH.getKey(jsonH.json, self.key_word.toPlainText())
        if self.key_key.toPlainText() == '':
            for chain in jsonH.allList:
                output.append(" => ".join(chain))
        else:
            for chain in jsonH.allList:
                if chain[-2] == self.key_key.toPlainText():
                    output.append(" => ".join(chain))
        self.show_json.setText("\n".join(output))


    def openFile(self):
        openFileHandler = openFileDialog()
        if hasattr(openFileHandler, 'fileName'):
            self.path.setText(openFileHandler.fileName)

    def formatJson(self):
        jsonH = jsonHandler()
        jsonH.getJson(self.path.toPlainText())
        jsonH.formatJson()
        ret = jsonH.formatedJson
        self.show_json.setText(ret)

 
class jsonHandler(object):
    def __init__(self):
        self.allList = list()
        self.nodeList = ['JSON']
        self.formatedJson = None
        self.json = None

    def getJson(self, path):
        with open(path, 'r') as dataFile:
            self.json = json.loads(dataFile.read())

    def getKey(self, data, keyWord, lastItem=None):
        ifPopList = True
        if isinstance(data, list):
            if data == []:
                self.nodeList.pop(len(self.nodeList) - 1)
                return None
            for id,v in enumerate(data):
                self.nodeList.append("[%d]" % id)
                self.getKey(v, keyWord, 'list')
        elif isinstance(data, dict):
            for key, value in data.items():
                self.nodeList.append(key)
                self.getKey(value, keyWord, 'dict')
        else:
            data = str(data)
            if data == keyWord:
                self.nodeList.append(data)
                self.allList.append(self.nodeList.copy())
                self.nodeList.pop(len(self.nodeList) - 1)
        
        if self.nodeList and ifPopList:
            self.nodeList.pop(len(self.nodeList) - 1)

    def formatJson(self):
        self.formatedJson = json.dumps(self.json, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
 
    prog = json_ui_dialog(dialog)
 
    dialog.show()
    sys.exit(app.exec_())
