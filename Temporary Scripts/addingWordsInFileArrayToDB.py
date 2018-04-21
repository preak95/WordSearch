# This script is meant to be run only once.
"""
As of now, we do not have the list of words in a particular book seprately in our MongoDB.
Which is why, in order to not run the whole thing again, we'll use this script to add only the wordlist to the Db
"""
import os
from pymongo import MongoClient
import re

connection = MongoClient()
db = connection.wordsearch

def filewordlistcreator(dir):
    for txtfile in os.listdir(dir): #iterate through pdfs in pdf directory
        fileExtension = txtfile.split(".")[-1]
        wordarray = []
        if fileExtension == "txt":
            textfile = open(dir + txtfile)
            wordarray = re.compile('\w+').findall(textfile.read())

            # Extract the name of the book
            filename = re.compile("(.*/)*").split(textfile.name)[-1]

            # This line is supposed to add the wordarray along with the filename
            # so as to allow us too gain access to all the words of a particular book
            db.wordsInFileList.insert({"filename": filename, "wordlist": wordarray})
            print "Added to DB: " + filename

filewordlistcreator("C:/Users/ps109/Desktop/Project/WordSearch/text/")
