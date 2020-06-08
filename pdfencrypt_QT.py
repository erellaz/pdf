# Encrypt a pdf
# 2019-06-01
# erellaz

initext='C:\\Users\\xxx\\Desktop\\'

import PyPDF2
import os

 
def set_password(input_file, user_pass, owner_pass):
    """
    This function encrypts a pdf file.
    """
    # The output encrypted file is name _enc, original file is kept
    path, filename = os.path.split(input_file)
    newfilename=filename.replace(".pdf","_enc.pdf")
    output_file = os.path.join(path, newfilename)
 
    output = PyPDF2.PdfFileWriter()
 
    filein=open(input_file, "rb")
    input_stream = PyPDF2.PdfFileReader(filein)
 
    for i in range(0, input_stream.getNumPages()):
        output.addPage(input_stream.getPage(i))
 
    outputStream = open(output_file, "wb")
 
    # Set user and owner password to pdf file
    output.encrypt(user_pass, owner_pass, use_128bit=True)
    output.write(outputStream)
    outputStream.close()
    filein.close()
    
#______________________________________________________________________________
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PDF encryptor'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 140
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create textbox
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(20, 20)
        self.textbox1.resize(280,20)
        self.textbox1.setText(initext)

        # Create textbox
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(20, 50)
        self.textbox2.resize(280,20)
        
        # Create a button in the window
        self.button = QPushButton('Encrypt', self)
        self.button.move(20,100)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        infile = self.textbox1.text()
        pwd=self.textbox2.text()
        set_password(infile,pwd,pwd)
        QMessageBox.question(self, 'PDF encryptor', "Encrypted ", QMessageBox.Ok, QMessageBox.Ok)
        #self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
