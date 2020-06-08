# Encrypt a pdf
# 2019-06-01
# erellaz

import PyPDF2
import os

infile=r"C:\Users\xxxx\xxxxx.pdf"
pwd="xxxxxxxx"

#______________________________________________________________________________
def set_password(input_file, user_pass, owner_pass):
    """
    This function encrypts a pdf file.
    """
    # The output encrypted file is name _enc, original file is kept
    path, filename = os.path.split(input_file)
    newfilename=filename.replace(".pdf","_enc.pdf")
    output_file = os.path.join(path, newfilename)
 
    output = PyPDF2.PdfFileWriter()
    
    print("Reading pdf: ",input_file)
    filein=open(input_file, "rb")
    input_stream = PyPDF2.PdfFileReader(filein)
 
    for i in range(0, input_stream.getNumPages()):
        print("Reading page:",i)
        output.addPage(input_stream.getPage(i))
 
    outputStream = open(output_file, "wb")
 
    # Set user and owner password to pdf file
    print("Encrypting... ")
    output.encrypt(user_pass, owner_pass, use_128bit=True)
    print("Writing encrypted output: ",output_file)
    output.write(outputStream)
    outputStream.close()
    filein.close()
#______________________________________________________________________________

set_password(infile,pwd,pwd)
 
# Useful for command line use
#def main():
#    parser = argparse.ArgumentParser()
#    parser.add_argument('-i', '--input_pdf', required=True,
#                        help='Input pdf file')
#    parser.add_argument('-p', '--user_password', required=True,
#                        help='output CSV file')
#    parser.add_argument('-o', '--owner_password', default=None,
#                        help='Owner Password')
#    args = parser.parse_args()
#    set_password(args.input_pdf, args.user_password, args.owner_password)
# 
#if __name__ == "__main__":
#    main()