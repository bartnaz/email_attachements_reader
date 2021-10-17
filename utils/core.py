from tkinter import *
from tkinter import font as tkFont

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

    def reader(self):
        EmailReader().get_attachements()
        self.scrn.delete(0, END)
        self.scrn.insert(0, 'Pobieranie zalacznikow')

    def gui(self):
        self.root = Tk()
        self.root.title('Attachments reader TERMINAL')

        # display declaration
        self.scrn = Entry(self.root, width=70, borderwidth=5)
        self.scrn.grid(row=1, column=0, columnspan=8, padx=10, pady=10)
        self.scrn.insert(0, 'Aby pobrać załaczniki kliknij przycisk')


        # fonts
        tmn9 = tkFont.Font(family='Times New Roman', size=9, weight='bold')


        # define buttons
        button_1 = Button(self.root, text='Zalaczniki z poprzedniego miesiaca', padx='40', pady='20')
        button_2 = Button(self.root, text='Pobierz zalaczniki', padx='140', pady='20', command=lambda:self.reader())
        button_3 = Button(self.root, text='', padx='60', pady='20')
        button_clear = Button(self.root, text='Clear window', padx='60', pady='10', command=self.button_clear)

        button_quit = Button(self.root, text='Exit', padx='40', pady='10', font=tmn9, command=self.close_window)


        # put the buttons on the screen
        button_1.grid(row=5, column=0)
        button_2.grid(row=5, column=1)
        button_3.grid(row=5, column=2)


        #clear/quit button
        button_clear.grid(row=6, column=1, sticky=E + W)
        button_quit.grid(row=6, column=2, sticky=E + W)

        self.root.mainloop()
