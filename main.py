from tkinter import font
import tkinter as tk
from pathlib import Path
import os
import customtkinter as ctk
from pages import HomePage, EmbedPage, ExtractPage, HowToUsePage, HelpContactPage, EmbedSuccessPage, ExtractSuccessPage

class MainApp(ctk.CTk):
    def __init__(self): 
        super().__init__()
        self.title("CloakCast")
        self.geometry("1500x1000")

        loadLalezarFont()
        loadSnigletFont()
        
        # Adding sidebar state to mainapp for consistency
        self.sidebarExpanded = False
    
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, EmbedPage, ExtractPage, HowToUsePage, HelpContactPage, EmbedSuccessPage, ExtractSuccessPage):
            frame = F(self, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)  

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()
        frame.sidebar.collapse_menu()

        if hasattr(frame, 'onShowFrame'):
            frame.onShowFrame()

def loadLalezarFont():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        fontPath = os.path.join(current_dir, "fonts", "Lalezar-Regular.ttf")

        ctk.FontManager.load_font(fontPath)
        
        return True

    except Exception as e:
        print(f"error loading lalezar font: {e}")
        return False
    
def loadSnigletFont():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        fontPath = os.path.join(current_dir, "fonts", "Sniglet-Regular.ttf")

        ctk.FontManager.load_font(fontPath)
        
        return True

    except Exception as e:
        print(f"error loading sniglet font: {e}")
        return False

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
