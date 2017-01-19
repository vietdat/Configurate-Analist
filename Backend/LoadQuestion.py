from __future__ import division
import sys
import Category
import ReadFromFile
import WriteToFile
from stopwords import stopwords
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from pymongo import MongoClient
import json

client = MongoClient()
db = client.test

qtCreatorFile = "UI/MainUI.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class LoadQuestion(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, file_path = ""):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.i = 0
	    #read file
        self.listItems = []
        self.listCategories = []
        readFromFile = ReadFromFile.ReadFromFile()
        self.f_content = readFromFile.ReadFileText(file_path)
        #self.f_category = readFromFile.ReadFileText("category.txt")
        self.f_category = self.getCategoryFromDB()
        self.btnNext.clicked.connect(lambda:self.clickNextButton())
        self.btnNewCategory.clicked.connect(lambda:self.clickNewCategory())
    
    def getCategoryFromDB(self):
        categories_arr = []
        for category in db.categories.find():
            categories_arr.append(category.get('category'))
        return categories_arr

    def showQuestion(self, text):
 	    self.txtQuestion.setText(text)

    def make_key(self, s):
        contents = s.split()
        key_words = [word for word in contents if word not in stopwords]
        self.listItems=[QCheckBox(word) for word in key_words]
        myLayout = QtGui.QFormLayout()
        for item in self.listItems:
            myLayout.addRow(item)
        widget = QtGui.QWidget()
        widget.setLayout(myLayout)
        self.scrollArea.setWidget(widget)

    def make_category_keyword(self):
        key_words = [word for word in self.f_category]
        self.listCategories = [QCheckBox(word) for word in key_words]
        myLayout = QtGui.QFormLayout()
        for item in self.listCategories:
            myLayout.addRow(item)
        widget = QtGui.QWidget()
        widget.setLayout(myLayout)
        self.scrollArea_category.setWidget(widget)

    def addNewCategoryToLayout(self, keys):
        key_words = [word for word in keys]
        self.listCategories = [QCheckBox(word) for word in key_words]
        myLayout = QtGui.QFormLayout()
        for item in self.listCategories:
            myLayout.addRow(item)
        widget = QtGui.QWidget()
        widget.setLayout(myLayout)
        self.scrollArea_category.setWidget(widget)
    
    def checkQuestionInDB(self, text):
        query = db.questions.find_one({"question": text})
        if(query):
            return True
        else:
            return False
    
    def checkCategoryInDB(self, text):
        query = db.categories.find_one({"category": text})
        if(query):
            return True
        else:
            return False
   
    def msgbtn(self):
        exit()

    def make_category(self):
        if not self.f_content:
            print("File is empty")
        else:
            #load first question to gui
            #Check question in DB
            while self.checkQuestionInDB(self.f_content[self.i].strip()):
                self.i = self.i + 1
                if self.i >= len(self.f_content):
                    break
            if self.i < len(self.f_content):
                #Add question to GUi
                self.showQuestion(self.f_content[self.i].strip())
                #Add key to GUI
                self.make_key(self.f_content[self.i].strip())
                self.i = self.i + 1
                self.make_category_keyword()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("All question in file is executed")
                msg.setWindowTitle("Done!")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.buttonClicked.connect(self.msgbtn)
                msg.exec_()
            
    def clickNewCategory(self):
        #Show dialog input
        text, ok = QInputDialog.getText(self, 'New category', 'Enter name of category:')
		
        if ok:
            #check text in db
            #if exist => warning
            if self.checkCategoryInDB(str(text)):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Error! Cannot add category")
                msg.setInformativeText("This category is exist! Please input again")
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            #else => insert to db and load form
            #Load new category to form
            else:
                db.categories.insert_one(
                    {
                        "category":str(text)
                    }
                )
                self.addNewCategoryToLayout(self.getCategoryFromDB())

    def clickNextButton(self):
        #Save question to mongodb
        #print(self.txtQuestion.toPlainText())
        db.questions.insert_one(
            {
                "question":str(self.txtQuestion.toPlainText())
            }
        )
        #Check user choosen category
        for category in self.listCategories:
            if category.isChecked():
                for item in self.listItems:
                    if item.isChecked():
                        writeToFile = WriteToFile.WriteToFile()
                        writeToFile.WriteToFileText(category.text(), item.text())
        self.make_category()
        
