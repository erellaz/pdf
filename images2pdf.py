from fpdf import FPDF
import os
import cv2

image_folder = r'D:\Dropbox\Jezierski\01_Passport'
pdf_name=r'Passport.pdf'
pdf_folder=r'D:\Dropbox\Jezierski'

# imagelist is the list with all image filenames
imagelist = [img for img in os.listdir(image_folder) if img.endswith(".JPG")]

pdf = FPDF('L')
for image in imagelist:
    pdf.add_page()
    img = cv2.imread(os.path.join(image_folder,image))
    h, w, c = img.shape
    print(image,h,w)
    if w>h:
        pdf.image(os.path.join(image_folder,image),5,5,280)
    else:
        pdf.image(os.path.join(image_folder,image),5,5,145)
pdf.output(os.path.join(pdf_folder,pdf_name), "F")