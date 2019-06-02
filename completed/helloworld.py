# Import Tkinter module
from tkinter import *

# Creation of root widget, i.e. a main window
root = Tk()

# Label widget, can show text or an image, and place on the root window
w = Label(root, text="Hello World!")
# Pack tells it so calculate size for the object
w.pack()

# Run Tkinter event loop.
root.mainloop()


# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")

#         self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
#         self.quit.pack(side="bottom")

#     def say_hi(self):
#         print("Hi Everybody!")

# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()