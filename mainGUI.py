from Tkinter import *
import time
from pymongo import MongoClient
import searchAlgorithm as Search
import meaningsearchGUI as gui
import unicodedata

# This is also a reading test
connection = MongoClient()
db = connection.wordsearch


# Search object initialized with reading speed of the user
search = Search.SearchAlgorithm(210)


root = Tk()
mainframe = Frame(root)
root.geometry("600x350")
root.resizable(width=False, height=False)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

solutionlist = []

def helper(word):
    print "Shit!"
    searchresult = search.search(word)
    if len(list(searchresult)) == 1:
        # wordarray = db.wordsInFileList.find({"filename": solutionlist[0][0].split("'")[1]})
        filename = unicodedata.normalize('NFKD', solutionlist[0][0]).encode('ascii', 'ignore')
        print filename
        wordarray = list(db.wordsInFileList.find({"filename": str(filename)}))[0]["wordlist"]
        print len(wordarray)

        testwindow = gui.MeaningSearch(wordarray, 210, solutionlist[0][2])

        testwindow.clocker()
        testwindow.root.mainloop()


word = Entry(mainframe)
searchButton = Button(mainframe, command=helper(word.get()), text="Search")
word.pack()
searchButton.pack()

root.mainloop()

