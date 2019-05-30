from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="Quit", highlightbackground="Yellow", command=frame.quit
        )
        
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", highlightbackground="Red", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("hi tehre")

#Create the base window that all other items will be drawn on to
root = Tk()

app = App(root)

root.mainloop()
root.destroy()