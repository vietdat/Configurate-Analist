from __future__ import division
import sys
import Category
import ReadFromFile
from stopwords import stopwords
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *

qtCreatorFile = "UI/MainUI.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class LoadQuestion(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, file_path = ""):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.i = 0
	    #read file
        readFromFile = ReadFromFile.ReadFromFile()
        self.f_content = readFromFile.ReadFileText(file_path)
        self.btnNext.clicked.connect(lambda:self.clickNextButton())

    def showQuestion(self, text):
 	    self.txtQuestion.setText(text)

    def make_key(self, s):
        contents = s.split()
        key_words = [word for word in contents if word not in stopwords]
        listItems=[QCheckBox(word) for word in key_words]
        myLayout = QtGui.QFormLayout()
        for item in listItems:
            myLayout.addRow(item)
        widget = QtGui.QWidget()
        widget.setLayout(myLayout)
        self.scrollArea.setWidget(widget)
        #self.listCheckBox.setLayout(myLayout)

    def make_category(self):
        ou = Category.Category('OU')
        tuition = Category.Category('Tuition')
        expense = Category.Category('Living Expense')
        other = Category.Category('Others')
        main_cate = [ou, tuition, expense, other]
        if not self.f_content:
            print("File is empty")
        else:
            #load first question to gui
            #Add question to GUi
            self.showQuestion(self.f_content[self.i])
            #Add key to GUI
            self.make_key(self.f_content[self.i])
            self.i = self.i + 1
    
    def clickNextButton(self):
        self.make_category()
        
