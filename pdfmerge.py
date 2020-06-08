# Merge many pdf
# 2019-06-01
# erellaz

import glob
from PyPDF2 import PdfFileMerger
#______________________________________________________________________________

infiles = glob.glob(r'C:\Users\User\*.pdf')
outfile="C:\Users\User\Desktop\Merge.pdf"
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

infiles.sort()
merger(outfile,infiles)