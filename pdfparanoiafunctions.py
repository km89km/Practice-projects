import os
from pathlib import Path
import PyPDF2

"Finds all .pdf files in a given folder and it's subfolders."
def pdfFinder(folder):
    # list to save found .pdf files to allow easy iteration.
    found_pdfs = []
    # walk through each folder in desired directory to find all .pdf files.
    for folderName, subfolders, filenames in os.walk(Path(folder)):
        for filename in filenames:
            # if .pdf is found we save a string of it's path to found_pdfs list.
            if filename.endswith('.pdf'):
                found_pdfs.append(Path(folderName, filename))
    # returns a list of .pdf's.
    return found_pdfs


"""Encrypt's the supplied .pdf file with the supplied password.
   The new file is saved to the cwd unless specified."""


def pdfEncrypter(filename, password, output_path='.'):
    # open file and create pdfReader object.
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # create new pdfWriter object to add pages to.
    pdfWriter = PyPDF2.PdfFileWriter()
    # copy pages from original to writer object.
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    pdfFileObj.close()
    # encrypt the new file with desired password.
    pdfWriter.encrypt(password)
    # name the new encrypted file with the '_encrypted.pdf' suffix.
    new_filename = Path(filename).stem + '_encrypted.pdf'
    new_path = Path(output_path, new_filename)
    # save the new file and then close it.
    encrypted_pdf = open(new_path, 'wb')
    pdfWriter.write(encrypted_pdf)
    encrypted_pdf.close()
    print(f'New encrypted file created: "{new_path}".')
    # return the new file path.
    return new_path


"checks whether the supplied .pdf is encrypted or not."


def encryptCheck(filename):
    # check that the file was encrypted correctly
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # An unsuccessful decryption will return '0'.
    if pdfReader.isEncrypted:
        print(f'File {filename.stem} is encrypted.')
        pdfFileObj.close()
        return True
    else:
        print(f'File {filename.stem} is not encrypted.')
        pdfFileObj.close()
        return False


"Attempts to decrpyt the .pdf with the supplied password. If succesful, the " \
"new file is written to the cwd unless specified otherwise."


def pdfDecrypter(filename, password, output_path='.'):
    # open file and create pdfReader object.
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # attempt to decrypt file with provided password.
    # if 0 is returned then the password is incorrect.
    if pdfReader.decrypt(password) == 0:
        pdfFileObj.close()
        print(f'Password is incorrect for file "{filename}".')
        return 0
    else:
        pdfWriter = PyPDF2.PdfFileWriter()
        # copy pages from original to writer object.
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))
        pdfFileObj.close()
        # name the new decrypted file with the '_decrypted.pdf' suffix.
        new_filename = Path(filename).stem + '_decrypted.pdf'
        new_path = Path(output_path, new_filename)
        # save the new file and then close it.
        decrypted_pdf = open(new_path, 'wb')
        pdfWriter.write(decrypted_pdf)
        decrypted_pdf.close()
        # return the new file path.
        return new_path
