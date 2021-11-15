""" 
Script to make a pdf from a reportory of pictures.
The pdf pages will auto size to the pictures.

The install of pypdf with pip does not work!!
Pypdf shall be installed as follow:
git clone https://github.com/reingart/pyfpdf.git
cd pyfpdf
python setup.py install
"""
from fpdf import FPDF
import os
import cv2


# User variables:
image_folder = r'D:\Dropbox\pics'
pdf_name=r'pdf_of_oucs.pdf'
pdf_folder=r'D:\Dropbox\pdf_folder'
pdf_author=r'Johnny Writer'
dpi=300

# imagelist is the list with all image filenames
imagelist = [img for img in os.listdir(image_folder) if img.endswith(".JPG")]

pdf = FPDF('P','mm',(297,210)) #new pdf, all units are mmm and the default page size is the tuple (297,210). This default will be overridden each time
pdf.set_title(pdf_name)
pdf.set_author(pdf_author)

for image in imagelist:
    img = cv2.imread(os.path.join(image_folder,image))
    h, w, c = img.shape
    
    to_mm = lambda x: int(x * 25.4/dpi)
    (h_mm,w_mm)=(to_mm(h),to_mm(w))
    print(image,h,w," pixels ",h_mm,"mm ",w_mm,"mm ")
    # if you get this error "add_page() got an unexpected keyword argument 'format'" then you have a bad install of FPDF, install from GITHUB, not from pip
    pdf.add_page(orientation='P', format=(w_mm+10,h_mm+10), same = False)
    pdf.image(os.path.join(image_folder,image),5,5,w=w_mm,h=h_mm)

print("Outputing pdf, this may take a while...")
pdf.output(os.path.join(pdf_folder,pdf_name), "F")
print("PDF done")