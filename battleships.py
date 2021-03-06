#Imports for Functionality
import tkinter as tk
from tkinter import ttk
from functools import partial
import sys
import os

#Main Class for game
class App(tk.Frame):
    #App Globals, to keep track of buttons and game state
    player = "X"
    bgColor="Red"
    gameWon = ""
    titleLabel = None
    gridSize = 10
    playerShipButtons = []
    playerGrid = []
    enemyGrid = []

    instructions = ["Place your ships now!", 
                    "Waiting for Player 2 to be ready", 
                    "Waiting for Player 2 turn", 
                    "Your turn!", 
                    "You've lost!", 
                    "You've won!",
                    "HIT!",
                    "MISS!"
                    "You've been hit!",
                    "Hah, missed!"
                    ]

    colours = ["Yellow", #Carrier
               "Purple", #Battleship
               "Cyan"  , #Cruiser
               "Cyan" , #Cruiser
               "Magenta", #Submarine
              ]

    shipsLen = [5, 4, 3, 3, 2]

    ships = ["Carrier",
             "Battleship",
             "Cruiser",
             "Cruiser",
             "Submarine"]

    selectedShip = 0

    containers = []
    label_container = []

    myShips = [None] * len(ships)

    isOrientationVertical = True


    class ship():
        def __init__(self):
            self.start = -1
            self.end = -1
            self.identity = -1
            self.isOrientationVertical = False
            self.destroyed = False

        def setShip(self, start, identity, orientation):
            self.start = start
            self.identity = identity
            self.isOrientationVertical = orientation

        

    #Initialisation function
    def __init__(self, master=None):
        super().__init__(master)
        self.create_mainwindow()
        self.master = master
        self.pack()
        

    def create_mainwindow(self):
        self.Mainwindow = tk.Frame(self.master)
        self.Mainwindow.pack()

        # Container for top level
        self.topBarContainer = tk.Frame(self.Mainwindow)
        self.containers.append(self.topBarContainer)
        # Container for own ships on left
        self.shipContainer = tk.Frame(self.Mainwindow, relief='sunken', width=2, bd=5)
        self.containers.append(self.shipContainer)
        
        # Container for Player Board 
        self.playerSide = tk.Frame(self.Mainwindow, relief='sunken')
        self.containers.append(self.playerSide)
        self.playerSideLabel = tk.Frame(self.playerSide)
        self.containers.append(self.playerSideLabel)
        self.playerBoard = tk.Frame(self.playerSide, relief='sunken', width=2, bd=5)
        self.containers.append(self.playerBoard)
        # Container for Enemy board
        self.enemySide = tk.Frame(self.Mainwindow, relief='sunken')
        self.containers.append(self.enemySide)
        self.enemySideLabel = tk.Frame(self.enemySide)
        self.containers.append(self.enemySideLabel)
        self.enemyBoard = tk.Frame(self.enemySide, relief='sunken', width=2, bd=5)
        self.containers.append(self.enemyBoard)
        # Container for enemy ships right
        self.enemyShipContainer = tk.Frame(self.Mainwindow, relief='sunken', width=2, bd=5)
        self.containers.append(self.enemyShipContainer)

        # Container for divider, may or may not be needed
        self.divider = tk.Frame(self.Mainwindow)
        self.containers.append(self.divider)
        self.create_widgets()
    
    def create_widgets(self):
        # Top Bar Widgets
        ttk.Button(self.containers[0], text="New Game", command=self.new_game).grid(row=0, column=0)
        self.instructionLabel = ttk.Label(self.containers[0], text=self.instructions[0]).grid(row=0, column=2, columnspan=3, sticky='news')
        # Player Ship Bar Widgets
        for i in range(0, len(self.ships)):
            button = ttk.Button(self.containers[1], text=(self.ships[i], "V"), width=12, command=partial(self.selectShip, i))
            self.playerShipButtons.append(button)
            button.grid(column=0, row=i, sticky='w', columnspan=2)
            self.myShips.append([i, -1, -1])
        # Enemy Ship bar widgets
        for i in range(0, len(self.ships)):
            self.label_container.append(ttk.Label(self.containers[8], text=self.ships[i], width=12).grid(column=4,row=i, sticky='e', columnspan=2))
        
        ttk.Label(self.containers[3], text="Your Board").grid(row=0, column=0)
        ttk.Label(self.containers[6], text="Enemy Board").grid(row=0, column=0)
        style = ttk.Style()
        style.configure('TButton', background="#ccc")
        
        # Player board widgets
        count = 0
        for i in range(0, self.gridSize):
            for k in range (0, self.gridSize):
                button = tk.Button(self.containers[4], text=" ", width=1, highlightbackground='blue', highlightcolor='blue', command=partial(self.placeShips, count))
                button.grid(column=k, row=i)
                App.playerGrid.append(button)
                count += 1

        # Enemy Board widgets
        count = 0
        for i in range(0, self.gridSize):
            for k in range (0, self.gridSize):
                button = tk.Button(self.containers[7], text=" ", width=1, height=1,command=partial(self.button_press, count))
                button.grid(column=k, row=i)
                App.enemyGrid.append(button)
                count += 1

        self.packAll()

    def packAll(self):
        self.topBarContainer.grid(row=0, column=0, columnspan=5)
        self.topBarContainer.pack(side="top")
        self.shipContainer.grid(row=1, column=0)
        self.shipContainer.pack(side="left")
        self.playerSide.grid(row=1, column=1)
        self.playerSideLabel.pack(side="top")
        self.playerBoard.pack(side="bottom")
        self.playerSide.pack(side="left")
        self.enemySide.grid(row=1, column=3)
        self.enemySide.pack(side="left")
        self.enemySideLabel.pack(side="top")
        self.enemyBoard.pack(side="bottom")
        self.enemyShipContainer.grid(row=1, column=4)
        self.enemyShipContainer.pack(side="left")
        #self.divider.pack()

    def selectShip(self, n):
        if(self.selectedShip == n):
            self.isOrientationVertical = not self.isOrientationVertical
        if(not self.isOrientationVertical):
            self.playerShipButtons[n].configure(text=(self.ships[n], "H"))
        else:
            self.playerShipButtons[n].configure(text=(self.ships[n], "V"))
        self.selectedShip=n
    
        # multiplier = 1
        # if(self.myShips[self.selectedShip][0] != -1):
        #     bname = self.playerGrid[self.myShips[self.selectedShip][1]]
        #     # Calculate if placement was vertical or horizontal
        #     if(self.myShips[self.selectedShip[2] < self.myShips[self.selectedShip[][1] + 6]]):
        #         multiplier = 1
        #     else:
        #         multiplier = 10

        #     for i in range(0, self.shipsLen[self.selectedShip]):
        #         bname = self.playerGrid[n+i*self.gridSize]        
        #         bname.configure(highlightbackground='green')
            
    
    def placeShips(self, n):
        multiplier = 1
        remMultiplier = 1

        #If ship was replaced, reset it
        if(self.selectedShip == -1):
            return
        if(self.isOrientationVertical):
            multiplier = self.gridSize
        
        if(self.myShips[self.selectedShip] != None):
            ship = self.myShips[self.selectedShip]
            if ship.isOrientationVertical:
                remMultiplier = 10
            for i in range(0, self.shipsLen[self.selectedShip]):
                bname = self.playerGrid[ship.start+i*remMultiplier]
                bname.configure(highlightbackground="blue")
            ship.__init__()
        
        #Check that the ship can be placed without falling off the grid
        if((n + self.shipsLen[self.selectedShip]*multiplier) <= len(self.playerGrid)):
            horizontalCheck = (n+self.shipsLen[self.selectedShip])%10
            #Check that the horizontal laying won't overrun to the next line
            if(((n%10) <= horizontalCheck) or (horizontalCheck == 0)):
                for i in range(0, self.shipsLen[self.selectedShip]):
                    bname = self.playerGrid[n+i*multiplier]
                    bname.configure(highlightbackground=self.colours[self.selectedShip])
                newShip = self.ship()
                newShip.setShip(n, self.selectedShip, self.isOrientationVertical)
                self.myShips.insert(self.selectedShip, newShip)
                    
            # if(n + self.gridSize*self.shipsLen[self.selectedShip] < len(self.playerGrid)):
            #     for i in range(0, self.shipsLen[n]):
            #         bname = self.playerGrid[n+i*self.gridSize]        
            #         bname.configure(fg=self.colours[n])            
            # bname.configure(text = ships[n][0])
            # self.playerGrid
        # else:
        #     print("oldPlacement")


    def button_press(self, button_id):
        print(button_id)
    def new_game(self):
        print("NewGame")
    #Class for carrying out a move once button is pressed
    #This denies moves once the game has been won
    #This also switches thetk.Label over for the next players turn
    # def make_move(self, n):
    #     bname=(App.button_identities[n])
    #     if(bname['text'] != '.' or App.gameWon != ""):
    #         return
    #     bname.configure(text = App.player)
    #     if(App.player == "X"):
    #         App.player="O"
    #         App.bgColor="Blue"
    #         App.titleLabel.configure(text=App.player)
    #     else:
    #         App.player="X"
    #         App.bgColor="Red"
    #         App.titleLabel.configure(text=App.player)


    #     self.check_for_win()

    # #Function to check if either player has won
    # #This checks in set patterns
    # def check_for_win(self):
    #     setList = set()
    #     # Check horizontally
    #     for i in range (0, 9, 3):
    #         setList.clear()
    #         for k in range (0, 3):
    #             setList.add(App.button_identities[i+k]['text'])
    #         if(len(setList) == 1 and '.' not in setList):
    #             print(App.button_identities[i+k]['text'], "Hwon the game")
    #             App.gameWon = App.button_identities[i]['text']
                
    #     # Check vertically
    #     for i in range (0, 3, 1):
    #         setList.clear()
    #         for k in range(0, 9, 3):
    #             setList.add(App.button_identities[i+k]['text'])
    #         if(len(setList) == 1 and '.' not in setList):
    #             print(App.button_identities[i+k]['text'], "Vwon the game")
    #             App.gameWon = App.button_identities[i]['text']
    #     # Check Diagonally
    #     setList.clear()
    #     for i in range (2, 8, 2):
    #         setList.add(App.button_identities[i]['text'])
    #     if(len(setList) == 1 and '.' not in setList):
    #         print(App.button_identities[i]['text'], "RDwon the game")
    #         App.gameWon = App.button_identities[i]['text']
    #     setList.clear()
    #     for i in range (0, 12, 4):
    #         setList.add(App.button_identities[i]['text'])
    #     if(len(setList) == 1 and '.' not in setList):
    #         print(App.button_identities[i]['text'], "LDwon the game")
    #         App.gameWon = App.button_identities[i]['text']

    #     setList.clear()
    #     for i in range (0, 9, 1):
    #         setList.add(App.button_identities[i]['text'])
    #     if('.' not in setList):
    #         print("Draw Game")


    #     #Pop up message for winner
    #     if App.gameWon:
    #         self.popupmsg()
    # #Popup message to display winner of game
    # def popupmsg(self):
    #     popup = tk.Tk()
    #     popup.wm_title("!")
    #     Label =ttk.Label(popup, text=("%s %s" % (App.gameWon, " is the Winner")))
    #     Label.pack(side="top", fill="x", pady=10)
    #     B1 =ttk.Button(popup, text="Okay", command = popup.destroy)
    #     B1.pack()
    #     popup.mainloop()
    # #Reset game state for a new game
    # def new_game(self):
    #     for i in range(0,9):
    #         bname=(App.button_identities[i])
    #         bname.configure(text=".", highlightbackground="grey")
    #         App.gameWon = ""

#Create the base window that all other items will be drawn on to
root = tk.Tk()
root.title("Battleships!")
app = App(master=root)
root.mainloop()
root.destroy()

# root = master
        # fra e
        # App.gameWon = ""
        # frame = Frame(master, bg="grey")
        # frame.pack()
        # #Create buttons andtk.Label to keep track of whose turn it is
        # ttk.Button(frame, text="New Game", command=self.new_game).grid(columnspan=3,row=0)
        # App.titleLabel = ttk.Label(frame, text=App.player)
        # App.titleLabel.grid(columnspan=3,row=1)
        # count = 0
        # #Create buttons in a for loop, keeping a reference to each button
        # for i in range(2,5):
        #     for k in range(3):
        #         button = ttk.Button(frame, text=".", command=partial(self.make_move, count))
        #         App.button_identities.append(button)
        #         button.grid(row=i,column=k)
        #         count += 1