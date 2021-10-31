from tkinter import *
from tkinter import font as tkFont

from PIL import Image, ImageTk

from utils import EmailReader


class GuiClass:
    def __init__(self):
        self.root = None
        self.scrn = None

    def close_window(self):
        self.root.destroy()

    def button_clear(self):
        self.scrn.delete(0, END)
        return

    def reader(self, range: int):
        EmailReader().get_attachements(range=range)
        self.scrn.delete(0, END)
        self.scrn.insert(0, "Pobieranie zalacznikow")

    def gui(self):
        self.root = Tk()
        self.root.title("Attachments reader TERMINAL")

        my_img = ImageTk.PhotoImage(Image.open("logo1.png"))
        my_label = Label(image=my_img)

        # display declaration
        self.scrn = Entry(self.root, width=50, borderwidth=5)
        self.scrn.grid(row=1, column=0, columnspan=8, padx=1, pady=1)
        self.scrn.insert(0, "Aby pobrać załaczniki kliknij przycisk")

        # fonts
        tmn9 = tkFont.Font(family="Arial", size=12)

        # define buttons
        button_1 = Button(
            self.root,
            text="Attachements from 3 months ago",
            padx="40",
            font=tmn9,
            pady="40",
            command=lambda: self.reader(range=3),
        )
        button_2 = Button(
            self.root,
            text="Attachements from last month",
            padx="40",
            font=tmn9,
            pady="40",
            command=lambda: self.reader(range=1),
        )
        button_3 = Button(
            self.root,
            text="Attachements from 2 months ago",
            padx="40",
            font=tmn9,
            pady="40",
            command=lambda: self.reader(range=2),
        )
        button_clear = Button(
            self.root,
            text="Clear window",
            padx="60",
            pady="20",
            font=tmn9,
            command=self.button_clear,
        )

        button_quit = Button(
            self.root,
            text="Exit",
            padx="40",
            pady="20",
            font=tmn9,
            command=self.close_window,
        )

        # put the buttons on the screen
        button_1.grid(row=5, column=0)
        button_2.grid(row=5, column=1)
        button_3.grid(row=5, column=2)

        # clear/quit button
        button_clear.grid(row=6, column=1, sticky=E + W)
        button_quit.grid(row=6, column=2, sticky=E + W)

        my_label.grid(row=0, column=1)

        self.root.mainloop()
