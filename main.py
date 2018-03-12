# This script is meant to upload all the words to the server

from pymongo import MongoClient

# Create a new connection to a single MongoDB instance at host:port.
connection = MongoClient("mongodb://indexer:bhininjosq@ds247407.mlab.com:47407/invertedindex")

# Create and get a data base (db) from this connection
db = connection.invertedindex

wordsInEnglish = open("C:/Users/ps109/Desktop/Project/WordSearch/words.txt").read().split()
wordnumber = 0
def uploadwords ():
    for word in wordsInEnglish:
        db.allwords.insert({
            "wordnumber": wordnumber,
            "word": word
        })

uploadwords()
connection.close()

