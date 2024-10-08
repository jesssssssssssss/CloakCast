import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

# window

window = tk.Tk()
window.title('Main')
window.geometry('1500x1000')

contentWindow = ttk.Frame(master = window)

# title
titleLabel = ttk.Label(master = window, text = 'CloakCast')
titleLabel.pack()

testLabel = ttk.Label(master = window, text = 'test label for github change. this can be removed np')
testLabel.pack()

# input field

inputFrame = ttk.Frame(master = window) # this is the box that takes user input of a number
intDeclare = tk.IntVar()
entry = ttk.Entry(master = inputFrame, textvariable=intDeclare) # this is actually declaring a user input, which is contained within the inputframe 
button = ttk.Button(master = inputFrame, text = 'ImAButton')
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
inputFrame.pack(pady = 10)


# run
window.mainloop()

