A repository containing practice projects from several learning resources (Automate the boring stuff (Sweigart),
Python Crash Course (Matthes)).
The practice projects are outlined in as far as what the program should do and information covered during the
chapter should be utilised to create a funcioning program.

2048.py - a simple program that uses webrowser and selenium to automate keypresses for the '2048' browser game. WE
open a new firefox browser and go to the homepage of the game. Using WebDriverWait, the program waits for the inital
pop up items to appear and remove them. Once they are clear, the html element of the page is found to allow interaction
wiith the game. The pattern of key presses are saved to a tuple called 'keys_to_send' and while the game is on going
each key press is sent to the browser and a small pause is used in between presses by using the time.sleep() function.
We know the game has ended when a game over element is visible and the while loop is broken.

blankRowInserter.py - using openpyxl, the program inserts the desired number of blank rows at the desired position.
the revelant arguments are supplied to the commmand line and the resulting file is saved as 'newcells.xlsx'.

bruteForce.py - attempts to decrypt an encrypted .pdf file by reading in a dictionary file and attempting both upper 
and lower case versions of each word. A list of words is created from the dictionary and then each is passed in both
forms to the decrypt method. If the password is a match the loop breaks.

cellInverter.py - also using openpyxl, the program inverts the cells so that the column and row values are switched. After
the total area to be copied is found, each cell is inverted; the column letter is converted to a row number and vice versa.
The results are then saved to a new file called 'invertedcells.xlsx'.

changer.py - contains a function that given a float representing the change of a transaction, will output the change
in the highest possible denominations in the form of a dictionary. The main funcionality of the function surrounds a
dictionary containing all the possible denominations ('money') and uses the dictionary method setdefault() to tally up
the denominations whilst iterating through the money dictionary and updating the given change value simultaneously. 
Although not contained in either of the resources listed above, it is a popular beginner project.

excelToCSV.py - converts all .xlsx files found in a provided directory to .csv files. Using the os.listdir() method,
each excel file is found in the provided directory and written to a new .csv file usinf the the excel filename ann 
sheet title.

multiplicationTable.py - creates an excel file containing the multiplication table of a provided integer in the command
line. The freeze_panes attribute is called on the sheet object so that the the first row and column is always visible when
scrolling through the results.

paranoia2.py - goes through every .pdf file in a folder and its subfolders and encrypts them with a password supplied in 
the command line. Each new file is saved with an '_encrypted.pdf' suffix. The files are then ensured to be encrypted 
before the original is deleted. All .pdf files are found in the specified folder and then using functions from the
auxiliary pdfparanoiafunctions.py file, each file is checked to see if it is already encrypted, if not it is encryted
using the supplied password, checked that encryption was successful and if so, the original is sent to the recycle bin
using the send2trash module.

textToSpreadsheet.py - reads in specified text files and writes each line to a cell in a column. I.e. the first file 
will be contained in column A and thesecond in column B and so on. A tuple is created containing the desired text
files, iterated through and using the readlines() function, each line is written to a cell using openpxl.


