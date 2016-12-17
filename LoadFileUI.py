import sys
sys.path.insert(0,'Backend');
import ReadFromFile
import WriteToFile
import LoadFile
import LoadQuestion

from PyQt4 import QtCore, QtGui, uic

qtLoadFile = "UI/UploadFile.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtLoadFile)

class UI(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnCancel.clicked.connect(self.close)
        self.btnImport.clicked.connect(self.loadFile)
        self.btnOk.clicked.connect(self.loadFileAndExe)
    def close(self):
        sys.exit()
    def loadFile(self):
        ins = LoadFile.LoadFile()
        strs = ins.loadFileUI()
        self.txtPath.setText(strs)
    def loadFileAndExe(self):
        #self.destroy()
        newwindow = LoadQuestion.LoadQuestion()
        newwindow.show()

