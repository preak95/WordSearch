""" Documentation
Hello there. For the purpose of eas in understanding this project at later times in life, and also
for the purpose of the understanding of others, I intend to heavily and very extensively documents
this python file and all the python files to come. Thank you. Enjoy coding.


The purpose of this script:
This script is meant to enable the user to choose a particular df file of their choice
and create an inverted idex like data structure for the same.

How?
1. Open the respective text file and extract all the words(let them repeat. We want all the
    words in their order) into a list

2. We'll use dictionaries for maintaining abstraction
                uniqueWordEntry {
                    "word"     : ___What word it is___,
                    "BookId"   : ___The ID of the book___,
                    "Position" : ___Array of numbers representing the position of words in the book"
                }

                //We'll try and implement auto-increment for bookID so we won't need to maintain them
                 anywhere else

3. We will scan through each of the words in the text file,
    If "The word is present in the index" :
        Update the item whose ID corresponds to the book we are scanning
        (In this case, even if the book didn't exist, it will create it for us)
    elif "word absent" :
        Enter the words and enter the details as mentioned in the above mentioned dictionary
"""

from Tkinter import Tk
from tkFileDialog import askopenfilename
import re
import hashlib
from pymongo import MongoClient
import os
import time
Tk().withdraw()


# Create a new connection to a single MongoDB instance at host:port.
connection = MongoClient()
db = connection.wordsearch

"""
textfilename = askopenfilename()  # Opens window to get the name of the text file

print(textfilename)  # Prints the exact location of the file

# Let us now split all the words in the text file

textfile = open(textfilename)

#wordarray = textfile.read().split()
wordarray = re.compile('\w+').findall(textfile.read())

# Extract the name of the book
filename = re.compile("(.*/)*").split(textfile.name)[-1]

print filename

# Get the md5 hash for the file name for unique id purposes
hash1 = hashlib.md5()
hash1.update(filename)
print("Hash: " + str(hash1.hexdigest()))

"""
class Worddictionary:
    """This will manage the list of all the dictionary entries"""
    def __init__(self):
        self.dictionaryList = []

    def dictInsert(self, wordtosearch, pos):
        for obj in self.dictionaryList:
            if obj['word'] == wordtosearch:
                # print("Going into if")
                obj['position'].append(pos)
        else:
            # print("Going into else")
            self.dictionaryList.append({
              'word': wordtosearch,
              'fileid': hash1.hexdigest(),
              'position': [pos]
            })

# This is a different part where I will try and make use of hash
# tables to deal with the problem

def createindexfromafile(wordarray, filename):
    wordHashTable = {}
    wordfrequency = {}
    pos = 1
    for word in wordarray:
        if word.lower() not in wordHashTable:
            wordHashTable[word.lower()] = [pos]
        else:
            wordHashTable[word.lower()].append(pos)

        if word.lower() not in wordfrequency:
            wordfrequency[word.lower()] = 1
        else:
            wordfrequency[word.lower()] += 1

        pos += 1

    wordDictionaryList = []
    filename = re.compile("(.*/)*").split(filename.name)[-1]
    for k in wordHashTable:
        wordDictionaryList.append({
            'word': k,
            'positions': wordHashTable[k],
            'fileName': str(filename)
        })

    for word in wordfrequency:
        # This would deal with maintaining a frequency of words
        db.freq.update({
            "word": word
        }, {
            "$inc": {"count": wordfrequency[word]}
        }, True)
        """
        else:
        # print "Entering:" + word['word']
        db.freq.insert({
            "word": word['word'],
            "count": len(word['positions'])
        }, True)
        """

    for word in wordDictionaryList:
        db.index.insert({
            "word": word['word'],
            "positions": word['positions'],
            "fileName": word['fileName']
        })


def filechooser(dir):
    for txtfile in os.listdir(dir): #iterate through pdfs in pdf directory
        fileExtension = txtfile.split(".")[-1]
        wordarray = []
        if fileExtension == "txt":
            textfile = open(dir + txtfile)
            wordarray = re.compile('\w+').findall(textfile.read())

            # Extract the name of the book
            filename = re.compile("(.*/)*").split(textfile.name)[-1]

            createindexfromafile(wordarray, textfile)
            # This line is to make sure we add the name of the file that is being added,
            # so we do not add it again in future
            db.allFileDirectory.insert({"filename": str(filename), "timestamp": time.ctime()})

            # This line is supposed to add the wordarray along with the filename
            # so as to allow us too gain access to all the words of a particular book
            db.wordsinfilelist.insert({"filename": filename, "wordlist": wordarray})
            print "Added to index: " + filename

# Execution

filechooser("C:/Users/ps109/Desktop/Project/WordSearch/text/")
