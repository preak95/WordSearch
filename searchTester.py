import time
from pymongo import MongoClient
import searchAlgorithm as Search
import meaningsearchGUI as gui
import unicodedata

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

# Search object initialized with reading speed of the user
search = Search.SearchAlgorithm(210)


# The real execution here
choice = 1
while choice != 0:
    choice = int(raw_input("Press Enter to search a word "))
    if choice == 0:
        choice = 0
        break
    else:
        word = raw_input("Enter the word to be searched: ")
        solutionlist = search.search(word)

        if len(list(solutionlist)) == 1:
            # wordarray = db.wordsInFileList.find({"filename": solutionlist[0][0].split("'")[1]})
            filename = unicodedata.normalize('NFKD', solutionlist[0][0]).encode('ascii', 'ignore')
            print(filename)
            wordarray = list(db.wordsInFileList.find({"filename": str(filename)}))[0]["wordlist"]
            print(len(wordarray))

            testwindow = gui.MeaningSearch(wordarray, 210, solutionlist[0][2])

            testwindow.clocker()
            testwindow.root.mainloop()

            break







