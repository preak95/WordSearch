from pymongo import MongoClient
import time

"""
Hello fellas.
In this piece of code, we will develop and algorithm to extract desired data from the MongoDB database
that we created earlier. Let us now see in detail what we are gonna do.

23/03/18 This is the first version of the algorithm so I expect it to have a higher time complexity

1. How was the structure of out DB?
    We had a document named index that stored data in this format:
        db.index.insert({
            "word": word['word'],
            "positions": word['positions'],
            "fileName": word['fileName']
        })
        
2. As an input we will have a series of "words" that we will need to search through the database
    and accordingly find out what book these words belong to
    
3. To do so we begin with the first word.
        i. We create a set of all the books that have the word w1 in them by using the following query on the DB
            db.find({"word" : w1})
            This will return all the objects containing the word w1(For a huge number of books, this number
            will be very large)
        ii. We then receive w2, we repeat the process and create a set of all the books with w2 in them.
            This is then followed by a process that will create an intersection of all the books in the two sets.
"""


# Create a new connection to a single MongoDB instance at host:port.
connection = MongoClient()
db = connection.wordsearch

"""
w1 = "Although"
w2 = "splendid"

search1 = list(db.index.find({"word": w1}))
search2 = list(db.index.find({"word": w2}))

searchset1 = set()
searchset2 = set()

for entry in search1:
    searchset1.add(entry["fileName"])

for entry in search2:
    searchset2.add(entry["fileName"])

intersectionSet = searchset1.intersection(searchset2)

worddifference = 80

books = []

for entry in intersectionSet:
    books.append(entry)

bookworddictionary = {}

for book in books:
    for entry in search1:
        if entry["fileName"] == book and entry["word"] == w1:
            bookworddictionary[(w1, book)] = entry["positions"]

for book in books:
    for entry in search2:
        if entry["fileName"] == book and entry["word"] == w2:
            bookworddictionary[(w2, book)] = entry["positions"]

#print bookworddictionary

# print bookworddictionary.keys()

l1 = []
l2 = []

solutiontuple = []


 
What worries me is the complexity of the code snippet below.
Suppose there are k books, l1 has m and l2 has n entries, then the complexity of the snipped would be 
 O(knm)

for book in books:
    l1 = bookworddictionary[(w1, book)]
    l2 = bookworddictionary[(w2, book)]

    for i in l1:
        for j in l2:
            if worddifference - 5 < j - i < worddifference + 5:
                solutiontuple.append((book, i, j))

print solutiontuple

"""

class SearchAlgorithm:
    sessionqueue = []
    Time = 0
    time1 = 0
    time2 = 0
    solutionlist = []

    def __init__(self, readingspeed):
        self.readingspeed = readingspeed

    def search(self, word):
        if len(self.sessionqueue) == 0:
            self.sessionqueue.append(word)
            self.time1 = time.clock()
        elif len(self.sessionqueue) == 2:
            self.sessionqueue.pop(0)
            self.Time = time.clock() - self.time1
            self.sessionqueue.append(word)
            self.time1 = time.clock()
            self.compute(self.sessionqueue[0], self.sessionqueue[1])
        elif len(self.sessionqueue) == 1:
            self.sessionqueue.append(word)
            self.Time = time.clock() - self.time1
            self.time1 = time.clock()
            self.compute(self.sessionqueue[0], self.sessionqueue[1])

        return self.solutionlist


    def compute(self, word1, word2):
        worddifference = int(self.readingspeed * self.Time / 60)

        print ("Word Difference is: " + str(worddifference))

        search1 = list(db.index.find({"word": word1}))
        search2 = list(db.index.find({"word": word2}))

        searchset1 = set()
        searchset2 = set()

        for entry in search1:
            searchset1.add(entry["fileName"])

        for entry in search2:
            searchset2.add(entry["fileName"])

        intersectionSet = searchset1.intersection(searchset2)

        # worddifference = 80

        books = []

        for entry in intersectionSet:
            books.append(entry)

        bookworddictionary = {}

        for book in books:
            for entry in search1:
                if entry["fileName"] == book and entry["word"] == word1:
                    bookworddictionary[(word1, book)] = entry["positions"]

        for book in books:
            for entry in search2:
                if entry["fileName"] == book and entry["word"] == word2:
                    bookworddictionary[(word2, book)] = entry["positions"]

        l1 = []
        l2 = []

        del self.solutionlist[:]
        for book in books:
            l1 = bookworddictionary[(word1, book)]
            l2 = bookworddictionary[(word2, book)]

            for i in l1:
                for j in l2:
                    if worddifference - 70 < j - i < worddifference + 70:
                        self.solutionlist.append([book, i, j])

        print(self.solutionlist)
        print(self.sessionqueue)
        return self.solutionlist

