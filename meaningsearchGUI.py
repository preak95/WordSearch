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
from wordnik import *
from PIL import Image, ImageTk

connection = MongoClient()
db = connection.wordsearch

apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'cbf25abcf44677fc4a12f0b721e0c2f4c5d9c5e13f14a9079'
client = swagger.ApiClient(apiKey, apiUrl)


class MeaningSearch:
    x = 0
    tempx = 0
    wordarray = []
    pauseflag = False
    wordandfrequencydictionary = {}
    frequencyThreshold = 20
    timer = 0
    delay = 0
    root = Tk()
    mainframe = Frame(root)
    centreframe = Frame(mainframe)
    labels = Label(centreframe, text="")
    wordApi = WordApi.WordApi(client)

    backbutton = Button()

    previousword = ""

    root.geometry("330x260")
    root.resizable(width=False, height=False)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    centreframe.grid(column=1, row=1, sticky=(N, W, E, S))
    centreframe.pack_propagate(0)

    mainframe.columnconfigure(0, weight=0)
    mainframe.rowconfigure(0, weight=0)
    arr = ['Amazing', 'wonderful', 'hemp', 'cotton', 'gin']

    # Images
    backwardimage = ImageTk.PhotoImage(Image.open('C:/Users/ps109/Desktop/Project/WordSearch/Images/back.png').resize((40, 40), Image.BILINEAR))
    forwardimage = ImageTk.PhotoImage(Image.open('C:/Users/ps109/Desktop/Project/WordSearch/Images/forward.png').resize((40, 40), Image.BILINEAR))
    pauseimage = ImageTk.PhotoImage(Image.open('C:/Users/ps109/Desktop/Project/WordSearch/Images/pause.png').resize((40, 40), Image.BILINEAR))
    playimage = ImageTk.PhotoImage(Image.open('C:/Users/ps109/Desktop/Project/WordSearch/Images/play.png').resize((40, 40), Image.BILINEAR))

    def __init__(self, wordarray, readspeed, startpoint):
        # Loads the file and creates a list of all the words

        self.wordarray = wordarray[startpoint:]
        frequencylist = list(db.freq.find())
        frequencyDictionary = {}

        for item in frequencylist:
            frequencyDictionary[str(item["word"].lower())] = int(item["count"])
            # print(item["count"])

        for word in wordarray:
            if frequencyDictionary[word.lower()] < self.frequencyThreshold:
                self.wordandfrequencydictionary[str(word.lower())] = 1
            else:
                self.wordandfrequencydictionary[str(word.lower())] = 0

        self.timer = float(readspeed) / 60.0

        self.delay = int((1.0 / self.timer) * 1000)

        self.meaningoutput = Label(self.centreframe, text=" "*200, wraplength=200, borderwidth=2, relief="groove")

        self.labels.grid(row=1, column=1, sticky="EW", columnspan=2, pady=(5, 5))

        self.meaningoutput.grid(row=2, column=1, sticky="S", columnspan=2, padx=(10, 10))

        #Buttons
        self.pausebutton = Button(self.mainframe, image=self.pauseimage, command=self.pause, height=40, width=40)
        forwardbutton = Button(self.mainframe, image=self.forwardimage, command=self.forward, height=40, width=40)
        backbutton = Button(self.mainframe, image=self.backwardimage, command=self.backward, height=40, width=40)

        # Events
        self.mainframe.bind("<Right>", self.forwardevent)
        self.mainframe.bind("<Left>", self.backwardevent)
        self.mainframe.bind("<space>", self.pauseevent)

        backbutton.grid(column=0, row=0, padx=10)
        self.pausebutton.grid(column=1, row=0)
        forwardbutton.grid(column=2, row=0)

        # ss
        self.mainframe.focus_set()

    def forward(self):
        self.x += 1

    def backward(self):
        self.x -= 10

    def pause(self):
        if self.pauseflag is False:
            self.pausebutton.configure(image=self.playimage)
            self.pauseflag = True
        elif self.pauseflag is True:
            self.pausebutton.configure(image=self.pauseimage)
            self.pauseflag = False

    # Keyboard event functions

    def forwardevent(self, event):
        self.x += 1

    def backwardevent(self, event):
        self.x -= 10

    def pauseevent(self, event):
        if self.pauseflag is False:
            self.pausebutton.configure(image=self.playimage)
            self.pauseflag = True
        elif self.pauseflag is True:
            self.pausebutton.configure(image=self.pauseimage)
            self.pauseflag = False

    def clocker(self):
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.printer(self.wordarray[self.x])
        if self.pauseflag is False:
            self.x += 1
        self.root.after(self.delay, self.clocker)

    def printer(self, word):
        # print "What the hell?!" + str(arr[0])
        if self.wordandfrequencydictionary[word.lower()] == 0:
            self.labels.configure(text=self.previousword, font='Helvetica 18 bold')
        else:
            self.labels.configure(text=word.title(), font='Helvetica 18 bold')
            self.previousword = word.title()

            if word[-1] == 's':
                word = word[0:-1]
            definition = []
            try:
                definition = self.wordApi.getDefinitions(word)
            except:
                self.meaningoutput.configure(text="Some error occurred while trying to connect to API")
                self.labels.configure(text="           ")

            if definition is not None:
                text = definition[0].text + " "*(200 - (len(definition[0].text) % 200))
                self.meaningoutput.configure(text=text, font='Helvetica 9 italic')
                time.sleep(4)
            else:
                self.meaningoutput.configure(text=" "*200)
                self.labels.configure(text="      ")




