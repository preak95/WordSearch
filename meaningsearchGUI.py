"""
What is this module?
Once the system knows what book the user is reading, it has to start helping him/her.
We can start to show the meanings of "these" words.
These: The difficult words so to speak.

We need GUI and some other things for this module
"""
import bs4 as bs
import mechanize
from Tkinter import *
import re
import time
import datetime
from pymongo import MongoClient

connection = MongoClient()
db = connection.wordsearch

class MeaningSearch:
    x = 0
    wordarray = []
    timer = 0
    labels = []
    root = Tk()
    mainframe = Frame(root)
    root.geometry("600x350")
    root.resizable(width=False, height=False)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    arr = ['Amazing', 'wonderful', 'hemp', 'cotton', 'gin']

    def __init__(self, wordarray, readspeed, startpoint):
        # Loads the file and creates a list of all the words

        self.wordarray = wordarray[startpoint:]

        self.timer = float(readspeed) / 60.0

        self.labels = [Label(self.mainframe, text="")] * 9
        for i in range(0, 9):
            if i != 5:
                self.labels[i] = Label(self.mainframe, text="INITIAL")
            else:
                self.labels[i] = Label(self.mainframe, text="INITIAL", width=12)
            self.labels[i].grid(row=2, column=i, sticky="EW")

        """
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        """

    def slider(self, k):
        return list(self.wordarray[k:k+9])

    def clocker(self):
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.printer(self.slider(self.x))
        self.x += 1
        # lab['text'] = time
        self.root.after(int((1.0/self.timer)*1000), self.clocker)

    def printer(self, arr):
        #print "What the hell?!" + str(arr[0])

        for i in range(0, 9):
            self.labels[i].configure(text=arr[i])
            if i == 4:
                self.labels[i].config(font=("Courier", 20, "bold"))


"""
testwindow = MeaningSearch("C:/Users/ps109/Desktop/Project/WordSearch/Reading test text.txt", 210)
testwindow.clocker()
testwindow.root.mainloop()
"""

