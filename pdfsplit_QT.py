# Split a pdf
# 2019-06-01
# erellaz
 
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
 
 
def pdf_splitter(input_file):
    path,fname = os.path.split(input_file)
 
    pdf = PdfFileReader(input_file)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        
        fname2=os.path.splitext(fname)[0]
        output_filename = '{}_page_{}.pdf'.format(fname2, page+1)
        output_file_with_path =os.path.join(path, output_filename)
        
        with open( output_file_with_path, 'wb') as out:
            pdf_writer.write(out)
 
        print('Created: {}'.format( output_file_with_path))
        
#______________________________________________________________________________
input_file = r"C:\Users\xx\Desktop\Merge.pdf"
#pdf_splitter(input_file)
#______________________________________________________________________________
#if __name__ == '__main__':
#    path = 'w9.pdf'
#    pdf_splitter(path)

#______________________________________________________________________________
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PDF spliter'
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
        self.textbox1.setText(input_file)

        # Create a button in the window
        self.button = QPushButton('Split', self)
        self.button.move(20,60)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        input_file = self.textbox1.text()
        pdf_splitter(input_file)
        QMessageBox.question(self, 'PDF splitter', "Splitted ", QMessageBox.Ok, QMessageBox.Ok)
        #self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())