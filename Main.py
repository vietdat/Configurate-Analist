import sys
sys.path.insert(0,'Backend');
import ReadFromFile
import WriteToFile
import LoadFile
import LoadQuestion
from LoadQuestion import LoadQuestion
from PyQt4 import QtCore, QtGui, uic

qtLoadFile = "UI/UploadFile.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtLoadFile)

class UI(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.path = ""
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
        self.path = strs
    def loadFileAndExe(self):
        self.LoadQuestion=LoadQuestion(self.path)
        self.LoadQuestion.make_category()
        self.LoadQuestion.show()
        self.hide()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())
