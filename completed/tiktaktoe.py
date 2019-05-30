#Imports for Functionality
from tkinter import *
from functools import partial
import sys
import os

#Main Class for game
class App:
    #App Globals, to keep track of buttons and game state
    player = "X"
    bgColor="Red"
    gameWon = ""
    titleLabel = None
    button_identities = []

    #Initialisation function
    def __init__(self, master):
        super().__init__()
        root = master
        App.gameWon = ""
        frame = Frame(master, bg="grey")
        frame.pack()
        #Create buttons and label to keep track of whose turn it is
        Button(frame, text="New Game", highlightbackground="grey", command=self.new_game).grid(columnspan=3,row=0)
        App.titleLabel = Label(frame, bg="Red", fg="white", text=App.player, padx=40, relief="sunken", font=("Helvetica", 16))
        App.titleLabel.grid(columnspan=3,row=1)
        count = 0
        #Create buttons in a for loop, keeping a reference to each button
        for i in range(2,5):
            for k in range(3):
                button = Button(frame, text=".", padx=20, pady=20, font=("Helvetica", 16), highlightbackground="grey", command=partial(self.make_move, count))
                App.button_identities.append(button)
                button.grid(row=i,column=k)
                count += 1

    #Class for carrying out a move once button is pressed
    #This denies moves once the game has been won
    #This also switches the label over for the next players turn
    def make_move(self, n):
        bname=(App.button_identities[n])
        if(bname['text'] != '.' or App.gameWon != ""):
            return
        bname.configure(text = App.player, highlightbackground=App.bgColor)
        if(App.player == "X"):
            App.player="O"
            App.bgColor="Blue"
            App.titleLabel.configure(text=App.player, bg=App.bgColor)
        else:
            App.player="X"
            App.bgColor="Red"
            App.titleLabel.configure(text=App.player, bg=App.bgColor)


        self.check_for_win()

    #Function to check if either player has won
    #This checks in set patterns
    def check_for_win(self):
        # Check horizontally
        for i in range (0, 9, 3):
            print(i)
            if(App.button_identities[i]['text'] == App.button_identities[i+1]['text'] == App.button_identities[i+2]['text'] and App.button_identities[i]['text'] != '.'):
                print(App.button_identities[i]['text'], "won the game")
                App.gameWon = App.button_identities[i]['text']
        # Check vertically
        for i in range (0, 3, 1):
            print(i)
            if(App.button_identities[i]['text'] == App.button_identities[i+3]['text'] == App.button_identities[i+6]['text'] and App.button_identities[i]['text'] != '.'):
                print(App.button_identities[i]['text'], "won the game")
                App.gameWon = App.button_identities[i]['text']
        # Check Diagonally
        if(App.button_identities[0]['text'] == App.button_identities[4]['text'] == App.button_identities[8]['text'] and App.button_identities[0]['text'] != '.'):            
            print(App.button_identities[0]['text'], "won the game")
            App.gameWon = App.button_identities[0]['text']
        if (App.button_identities[2]['text'] == App.button_identities[4]['text'] == App.button_identities[6]['text'] and App.button_identities[2]['text'] != '.'):
            print(App.button_identities[2]['text'], "won the game")
            App.gameWon = App.button_identities[2]['text']
        #Pop up message for winner
        if App.gameWon:
            self.popupmsg()
    #Popup message to display winner of game
    def popupmsg(self):
        popup = Tk()
        popup.wm_title("!")
        label = Label(popup, text=("%s %s" % (App.gameWon, " is the Winner")))
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()
    #Reset game state for a new game
    def new_game(self):
        for i in range(0,9):
            bname=(App.button_identities[i])
            bname.configure(text=".", highlightbackground="grey")
            App.gameWon = ""

#Create the base window that all other items will be drawn on to
root = Tk()

app = App(root)

root.mainloop()
root.destroy()