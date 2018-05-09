from pymongo import MongoClient
from wordnik import *

connection = MongoClient()
db = connection.wordsearch

apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'cbf25abcf44677fc4a12f0b721e0c2f4c5d9c5e13f14a9079'
client = swagger.ApiClient(apiKey, apiUrl)

"""
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
        }, Tru
    else:
        print "Entering"
        db.freq.insert({
            "word": word,
            "count": wordHashTable[word]
        })

print list(db.freq.find()

frequencylist = list(db.freq.find())
frequencyDictionary = {}
wordandfrequencydictionary = {}

wordarray = list(db.wordsInFileList.find({"filename": "1- Stormbreaker.pdf.txt"}))
wordarray = list(wordarray[0]["wordlist"])

for item in frequencylist:
    frequencyDictionary[str(item["word"].lower())] = int(item["count"])
    #print(item["count"])

for word in wordarray:
    if frequencyDictionary[word.lower()] < 1000:
        wordandfrequencydictionary[str(word.lower())] = 1
    else:
        wordandfrequencydictionary[str(word.lower())] = 0

#print(wordandfrequencydictionary["raining"])

sortedDict = {}
sortedlist = []

for key, value in sorted(frequencyDictionary.iteritems(), key=lambda (k,v): (v,k)):
    sortedDict[key] = value
    sortedlist.append(value)

print(sortedlist[74000])

print(list(db.freq.find({"count": 30})))


"""


wordApi = WordApi.WordApi(client)
example = wordApi.getDefinitions('renew')
print(example[0].text)