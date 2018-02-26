import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Window(QMainWindow):
    def __init__(self, fileName=None, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowIcon(QIcon("text-editor-icon.png"))
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        self.setGeometry(50,50,500,400)
        self.setWindowTitle("Editor++")
        self.setWindowIcon(QIcon("text-editor-icon.png"))
        newAction = QAction("&New",self)
        openAction = QAction("&Open",self)
        saveAction = QAction("&Save",self)
        saveAsAction = QAction("&Save As",self)
        cutAction = QAction("&Cut",self)
        copyAction = QAction("&Copy",self)
        pasteAction = QAction("&Paste",self)
        
        newAction.setShortcut("Ctrl+n")
        newAction.setStatusTip("New File")
        
        openAction.setShortcut("Ctrl+O")
        openAction.setStatusTip("Open File")
                
        saveAction.setShortcut("Ctrl+s")
        saveAction.setStatusTip("Save File")
        
        saveAsAction.setShortcut("Ctrl+Shift+s")
        saveAsAction.setStatusTip("Save As")
              
        cutAction.setShortcut("Ctrl+X")
        cutAction.setStatusTip("Cut")
                
        copyAction.setShortcut("Ctrl+C")
        copyAction.setStatusTip("Copy")
               
        pasteAction.setShortcut("Ctrl+V")
        pasteAction.setStatusTip("Paste")
                      
        menubar = self.menuBar()
        
        
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAsAction)
                
        editMenu = menubar.addMenu("&Edit")
        editMenu.addAction(cutAction)
        editMenu.addAction(copyAction)
        editMenu.addAction(pasteAction)
        '''               
        self.file_toolbar = self.addToolBar("File")
        self.file_toolbar.addAction(newAction)
        self.file_toolbar.addAction(openAction)
        self.file_toolbar.addAction(saveAction)
        self.file_toolbar.addAction(saveAsAction)
        
        
        self.toolbar = self.addToolBar("Edit")
        self.toolbar.addAction(cutAction)
        self.toolbar.addAction(copyAction)
        self.toolbar.addAction(pasteAction)
       '''               
        self.status = self.statusBar()
        
        self.show()
     
        
app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())

