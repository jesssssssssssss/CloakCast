import tkinter as tk
from tkinter import ttk
from tkinter import font
import ttkbootstrap as ttk
import customtkinter as ctk
from customtkinter import FontManager

from embedPage import EmbedPage


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CloakCast")
        self.geometry("1500x1000")

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (HomePage, EmbedPage): # Add later: "ExtractPage"
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ctk.CTkLabel(self, text="CloakCast", font=("Lalezar", 70), text_color='#a63a50')
        label.pack(pady=20)

        embed_button = ctk.CTkButton(self, text="Embed", command=lambda: controller.show_frame(EmbedPage))
        embed_button.pack(pady=10) 

        #extract_button = ctk.CTkButton(self, text="Extract", command=lambda: controller.show_frame(ExtractPage))
        #extract_button.pack(pady=10)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()



''' # window

window = ctk.CTk(fg_color='#FEFCFB')
window.title('Main')
window.geometry('1500x1000')

contentWindow = ctk.CTkFrame(master = window, fg_color='White')
contentWindow.grid(padx=500, pady=250)

# title
titleLabel = ctk.CTkLabel(
    master = contentWindow, 
    text = 'CloakCast', 
    text_color='#a63a50',
    corner_radius = 10, 
    font=("lalezar", 70)) # need to figure out how to import font / get it to work
titleLabel.grid(row=0, column=0, padx=100)

embedButton = ctk.CTkButton(master=contentWindow, text='Embed', text_color='#FFF', fg_color='#393839')
embedButton.grid(row=1, column=0, padx=20,pady=(0,20))


extractButton = ctk.CTkButton(master=contentWindow, text='Extract', text_color='#FFF', fg_color='#393839')
extractButton.grid(row=1, column=1,pady=(0,0))




 # input field

inputFrame = ctk.CTkFrame(master = contentWindow) # this is the box that takes user input of a number
intDeclare = tk.IntVar()
entry = ctk.CTkEntry(master = inputFrame, textvariable=intDeclare) # this is actually declaring a user input, which is contained within the inputframe 

button = ctk.CTkButton(master = inputFrame, text = 'ImAButton')
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
inputFrame.pack(pady = 10) 
#please leave input field here for now so we can refer to it later



# run
window.mainloop()

'''
