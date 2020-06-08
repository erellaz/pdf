# Merge many pdf
# 2019-06-01
# erellaz

import glob
from PyPDF2 import PdfFileMerger
#______________________________________________________________________________

infst = r'C:\Users\x\Desktop\tst*.pdf'
outfile = r"C:\Users\x\Desktop\Merge.pdf"
#______________________________________________________________________________

 
def merger(outfile, infiles):
    pdf_merger = PdfFileMerger()
 
    for ifile in infiles:
        pdf_merger.append(ifile)
 
    with open(outfile, 'wb') as fileobj:
        pdf_merger.write(fileobj)

    fileobj.close()
    pdf_merger.close()
#______________________________________________________________________________

#infiles.sort()
#merger(outfile,infiles)

#______________________________________________________________________________
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PDF merger'
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
        self.textbox1.setText(infst)

        # Create textbox
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(20, 50)
        self.textbox2.resize(280,20)
        self.textbox2.setText(outfile)
        
        # Create a button in the window
        self.button = QPushButton('Merge', self)
        self.button.move(20,100)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        infst = self.textbox1.text()
        outfile=self.textbox2.text()
        infiles = glob.glob(infst)
        infiles.sort()
        print("Path",infst)
        print("Files to merge",infiles,"into",outfile)
        merger(outfile,infiles)
        QMessageBox.question(self, 'PDF merger', "Merged ", QMessageBox.Ok, QMessageBox.Ok)
        #self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())