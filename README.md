## Manipulates pdfs with python

- Merge various pdfs.
- Split one pdf.
- Encrypt a pdf with a password.
- Create a PDF from a repertory full of pictures, and size each page of the pdf according to the picture size. Alternatively use a constant page size (like A4) and size the image to the fit the page.

Also has a QT interface for those who do not want to script.

The install of pypdf with pip seems to install an outdated version of pypdf. The proper installation of pypdf is this:

- git clone https://github.com/reingart/pyfpdf.git
- cd pyfpdf
- python setup.py install
