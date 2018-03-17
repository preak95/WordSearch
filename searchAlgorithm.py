from pymongo import MongoClient

# Create a new connection to a single MongoDB instance at host:port.
connection = MongoClient()
db = connection.wordsearch

