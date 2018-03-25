import time
from pymongo import MongoClient
import searchAlgorithm as Search

# This is also a reading test
connection = MongoClient()
db = connection.wordsearch

testtext = open("C:/Users/ps109/Desktop/Project/WordSearch/Reading test text.txt")
text = testtext.read()

print("Read the following comprehension. When done, press enter")

print("--------Passage---------\n\n")
t1 = time.clock()

print(text)
stopperinput = raw_input()

t2 = time.clock()
print("Your reading speed is:" + str(int(593/((t2 - t1)/60))))

readingspeed = int(593/((t2 - t1)/60))

search = Search.SearchAlgorithm(readingspeed = 180)

def searchword(word):
    search.search(word)


# The real exection here
choice = 1
while choice != 0:
    choice = int(raw_input("Press Enter to search a word "))
    if choice == 0:
        choice = 0
        break
    else:
        word = raw_input("Enter the word to be searched: ")
        searchword(word)





