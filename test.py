from pymongo import MongoClient

connection = MongoClient()
db = connection.test

words = ["pratik", "neeraj", "awesome"]
wordHashTable = {"neeraj": 32, "awesome": 99, "pratik": 42}

wordHashTable2 = {"pratik": 10, "neeraj": 3}

for word in wordHashTable:
    print "Something"
    # if len(list(db.freq.find({"word": str(word)}))) != 0:
    db.freq.update({
        "word": word
        }, {
        "$inc": {"count": wordHashTable[word]}
        }, True
    )

for word in wordHashTable2:
    # if len(list(db.freq.find({"word": str(word)}))) != 0:
    db.freq.update({
        "word": word
        }, {
        "$inc": {"count": wordHashTable2[word]}
        }, True
    )
"""
    else:
        print "Entering"
        db.freq.insert({
            "word": word,
            "count": wordHashTable[word]
        })
"""
print list(db.freq.find())
