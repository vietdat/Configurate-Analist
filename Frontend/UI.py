from __future__ import division
import sys
from stopwords import stopwords
from Category import *
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *

qtCreatorFile = "mainwindow.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class UI(QtGui.QMainWindow, Ui_MainWindow):
    ou = Category('OU')
    tuition = Category('Tuition')
    expense = Category('Living Expense')
    other = Category('Others')
    main_cate = [ou, tuition, expense, other]

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    #Show question to edit text.(UI)
    def showQuestion(self, text):
 	    self.txtQuestion.setText(text)

    #add key to key list (UI)
    def make_key(self, s):
        contents = s.split()
        key_words = [word for word in contents if word not in stopwords]
        listItems=[QCheckBox(word) for word in key_words]
        myLayout = QtGui.QFormLayout()
        for item in listItems:
            myLayout.addRow(item)
        self.listCheckBox.setLayout(myLayout)

    def make_category(self, read_file):
        with open(read_file, 'r') as f:
            f_content = f.readlines()
            for i in f_content:
                if (not any([elem.contain(i) for elem in self.main_cate])):
                    #Add question to GUi
                    self.showQuestion(i)
                    #Add key to GUI
                    self.make_key(i)
                    #data


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = UI()
    window.show()
    window.make_category("test.txt")
    sys.exit(app.exec_())
