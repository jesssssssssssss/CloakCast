#import tkinter as tk
#from tkinter import ttk
#from tkinter import font
#import ttkbootstrap as ttk
import customtkinter as ctk
from PIL import Image

from pages import HomePage, EmbedPage, ExtractPage, AboutPage, Sidebar


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CloakCast")
        self.geometry("1500x1000")
    
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, EmbedPage, ExtractPage, AboutPage):
            frame = F(self, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)  

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()



if __name__ == "__main__":
    app = MainApp()
    app.mainloop()




''' 


# input field *

inputFrame = ctk.CTkFrame(master = contentWindow) # this is the box that takes user input of a number
intDeclare = tk.IntVar()
entry = ctk.CTkEntry(master = inputFrame, textvariable=intDeclare) # this is actually declaring a user input, which is contained within the inputframe 

button = ctk.CTkButton(master = inputFrame, text = 'ImAButton')
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
inputFrame.pack(pady = 10) 

# please leave input field here for now so we can refer to it later *


'''
