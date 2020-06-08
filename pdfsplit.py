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
input_file = r"C:\Users\User\Desktop\x.pdf"
pdf_splitter(input_file)
#______________________________________________________________________________
#if __name__ == '__main__':
#    path = 'w9.pdf'
#    pdf_splitter(path)