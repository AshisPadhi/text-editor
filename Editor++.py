import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Window(QMainWindow):
    def __init__(self, fileName=None, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowIcon(QIcon("text-editor-icon.png"))
        self.textEdit = QTextEdit(self)
        
        self.textEdit.setStyleSheet("color: aqua;"
        			 "background-color: black;"
        			 "selection-color: yellow;"
        			 "selection-background-color: #ff6600;")
        self.setCentralWidget(self.textEdit)
        self.setWindowOpacity(0.4)
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
        exitAction = QAction("&Exit", self)
        undoAction = QAction("&Undo", self)
        redoAction = QAction("&Redo", self)

        
        newAction.setShortcut("Ctrl+n")
        newAction.setStatusTip("New File")
        
        openAction.setShortcut("Ctrl+O")
        openAction.setStatusTip("Open File")
        openAction.triggered.connect(self.open_file)
                
        saveAction.setShortcut("Ctrl+s")
        saveAction.setStatusTip("Save File")
        
        saveAsAction.setShortcut("Ctrl+Shift+s")
        saveAsAction.setStatusTip("Save As")
        saveAsAction.triggered.connect(self.save_file)
              
        cutAction.setShortcut("Ctrl+X")
        cutAction.setStatusTip("Cut")
        cutAction.triggered.connect(self.textEdit.cut)
                
        copyAction.setShortcut("Ctrl+C")
        copyAction.setStatusTip("Copy")
        copyAction.triggered.connect(self.textEdit.copy)
               
        pasteAction.setShortcut("Ctrl+V")
        pasteAction.setStatusTip("Paste")
        pasteAction.triggered.connect(self.textEdit.paste)
        
        undoAction.setShortcut("Ctrl+Z")
        undoAction.setStatusTip("Undo")
        undoAction.triggered.connect(self.textEdit.undo)

        redoAction.setShortcut("Ctrl+R")
        redoAction.setStatusTip("Undo")
        redoAction.triggered.connect(self.textEdit.redo)
        
        exitAction.setShortcut("Ctrl+Shift+E")
        exitAction.setStatusTip("Leave the app")
        exitAction.triggered.connect(self.close_application)
                      
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
        editMenu.addAction(undoAction)
        editMenu.addAction(redoAction)
                
        self.status = self.statusBar()
        
        font_choice = QAction("Font", self)
        font_choice.triggered.connect(self.fontchoice)
        editMenu.addAction(font_choice)
        
        
        self.show()
        
    def fontchoice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.textEdit.setFont(font)
     
    def open_file(self):
        name = QFileDialog.getOpenFileName(self,'Open File')
        file = open(name, 'r+')

        self.textEdit
        with file:
            text = file.read()
            self.textEdit.setText(text)
            
    def save_file(self):
        name = QFileDialog.getSaveFileName(self,"Save File")
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()
        
    def close_application(self):
        choose = QMessageBox.question(self, 'Exit',
                                            'You Sure You Really Wanna Quit?',
                                            QMessageBox.Yes | QMessageBox.No)
        if choose == QMessageBox.Yes:
            sys.exit()
        else:
            pass

        
app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())


