from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from Tkinter import Tk
from tkFileDialog import askopenfilename
Tk().withdraw()
from pdfminer.pdfpage import PDFPage
import os
from pymongo import MongoClient
import sys, getopt




# Create a new connection to a single MongoDB instance at host:port.
# connection = MongoClient("mongodb://indexer:bhininjosq@ds247407.mlab.com:47407/invertedindex")

# Create and get a data base (db) from this connection
# db = connection.invertedindex

# List of all the words in the english language
#wordsInEnglish = open("C:/Users/ps109/Desktop/Project/WordSearch/words.txt").read().split()

#converts pdf, returns its text content as a string


def convert(fname, txtdir, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

    # textFilename = txtdir + ".txt"
    # textFile = open(textFilename, "w")  # make text file
    # textFile.write(text)


#converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf
            text = convert(pdfFilename) #get string of text content of pdf
            textFilename = txtDir + pdf + ".txt"
            textFile = open(textFilename, "w") #make text file
            textFile.write(text) #write text to text file

pdfDir = "C:/Users/ps109/Desktop/Project/WordSearch/pdf/"
txtDir = "C:/Users/ps109/Desktop/Project/WordSearch/text/"

#Convert all the PDFs to text documents
convertMultiple(pdfDir, txtDir)

#We need to create unique list
def addToIndex (pdffile, name):
    # db = connection.invertedindex
    wordarray = pdffile.read().split()
    # Now we iterate through all these words and generate a list of all the unique words present in the text
    wordset = set(wordarray)
    uniqueset = set()
    for word in wordset:
        #if word in wordsInEnglish:
        uniqueset.add(word)
    #Next we need to add these
    for word in uniqueset:
        wd = db.index.find({"word": word})
        #if word in wordsInEnglish:
        db.index.insert({
            "word": word,
            "pdfs": [name]
        })
        '''
        else:
            db.index.update({"word": word}, {
                "$push": {"pdfs": name}
            })
        '''
    print "The documents were saved"

"""
def searchword(word):
    db = connection.invertedindex
    listofallpdfs = db.index.find({"word": word})
    for i in listofallpdfs:
        print(i)


addToIndex(open("C:/Users/ps109/Desktop/Project/text/hacking-the-art-of-exploitation.pdf.txt"), "hackingbook")
#searchword("modelsType")
# close connection
connection.close()


filename = askopenfilename()
convert(filename, txtDir)
"""