from Tkinter import *
from PIL import Image, ImageTk

class dormLifeProgram():
    
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.config(width = 1250, height = 940)

        self.title = Label(self.frame, text = "")
        self.title.config(padx = 5, pady = 5, font = ('Lucida Grande', '50'))

        self.laundryBtn = Button(self.frame)
        self.laundryIcon = ImageTk.PhotoImage(Image.open('IconImages/laundryIcon.jpg'))
        self.laundryBtn.config(padx = 5, image = self.laundryIcon)

        self.cleaningBtn = Button(self.frame)
        self.cleaningIcon = ImageTk.PhotoImage(Image.open('IconImages/cleaningIcon.jpg'))
        self.cleaningBtn.config(padx = 5, image = self.cleaningIcon)

        self.cookingBtn = Button(self.frame)
        self.cookingIcon = ImageTk.PhotoImage(Image.open('IconImages/cookingIcon.jpg'))
        self.cookingBtn.config(image = self.cookingIcon)

    def getFrame(self):
        return self.frame

    def getOpenDormLifeFrames(self):
        return self.openDormLifeFrames
