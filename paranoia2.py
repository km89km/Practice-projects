#! python3
# pdfparanoia.py - goes through every .pdf file in a folder and its subfolders
# and encrypts them with a password supplied in the command line. Each new file
# is saved with an '_encrypted.pdf' suffix. The files are then ensured to be
# encrypted before the original is deleted.

import sys
import os
from pathlib import Path
import PyPDF2
from send2trash import send2trash
# import functions for finding and encrypting .pdf's and checking the
# encryption.
import pdfparanoiafunctions as pdfFUNC

# if the necessary arguments are not provided the program will exit.
if len(sys.argv) != 3:
    print('Usage - "pdfparanoia.py" "path of folder to scan" "password".')
    sys.exit()

# create new folder for encrypted .pdf's if it doesn't already exist.
newfolder = Path(r'C:\Users\km89k\Desktop\pythonscripts', 'encrypted_pdfs')
if not os.path.exists(newfolder):
    os.makedirs(newfolder)

# create variable for output path.
output_path = Path(os.path.abspath(newfolder))

# save password provided in command line to variable for simpler use.
password = sys.argv[2]

# find all .pdf files in the specified folder.
found_pdfs = pdfFUNC.pdfFinder(sys.argv[1])

# iterate over each found file to copy each page.
for filename in found_pdfs:
    # if file was already encrypted then skip it.
    if pdfFUNC.encryptCheck(filename):
        pass
    else:
        # make new encrypted copy of file.
        new_path = pdfFUNC.pdfEncrypter(filename, password, output_path)

        # check that the newfile was encrypted correctly by attmempting to read
        # and decrypt. If the decryption is successful then we can remove the
        # original and send it to the recycling bin using send2trash.
        pdfFileObj = open(new_path, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        if pdfReader.decrypt(password) == 1:
            print(f'Original file to be deleted: '
                  f'"{os.path.abspath(filename)}".\n')
            send2trash(os.path.abspath(filename))
        else:
            print(f'File {new_path} was not encrypted correctly and should be '
                  f'attempted again.')
