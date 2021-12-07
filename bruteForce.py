#! python3
# bruteForce.py - attempts to decrypt an encrypted .pdf file by
# reading in a dictionary file and attempting both upper and lower
# case versions of each word. Practice project from chapter 15 of 'Automate
# the boring stuff' by Al Sweigart.

import PyPDF2
import os
import sys

# open text file containing english words in uppercase.
dictionary_file = open('dictionary.txt')
# read the contents and split at each new line to create list of words.
word_list = dictionary_file.read().split('\n')
dictionary_file.close()

# open encrypted .pdf file and create Reader object of it.
pdfFileObj = open(#ENCRYPTED_FILE, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
for i in range(len(word_list)):
    if pdfReader.decrypt(word_list[i]) == 1:
        print(f'Password found: "{word_list[i]}".')
        pdfFileObj.close()
        break
    elif pdfReader.decrypt(word_list[i].lower()) == 1:
        print(f'Password found: "{word_list[i].lower()}".')
        pdfFileObj.close()
        break
