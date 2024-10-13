''' import tkinter as tk
from tkinter import ttk
from tkinter import font
import ttkbootstrap as ttk '''
import customtkinter as ctk
import customtkinter


class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        homePageContent = ctk.CTkFrame(master = self, fg_color='White')
        homePageContent.pack(padx=500, pady=250)


        label = ctk.CTkLabel(homePageContent, text="CloakCast", font=("Lalezar", 70), text_color=("#a63a50", "#a63a50"), fg_color="white")
        label.pack(pady=20)

        embedButton = ctk.CTkButton(homePageContent, text="Embed", command=lambda: controller.show_frame(EmbedPage))
        embedButton.pack(pady=10) 

        #extract_button = ctk.CTkButton(self, text="Extract", command=lambda: controller.show_frame(ExtractPage))
        #extract_button.pack(pady=10)
        # we can add these later

class EmbedPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        embedPageContent = ctk.CTkFrame(master = self, fg_color='White') # this is the content window
        embedPageContent.pack(padx=500, pady=250)

        label = ctk.CTkLabel(embedPageContent, text="Embed Page", font=customtkinter.CTkFont(family='Calibri', size=30))
        label.pack(pady=20)

        #Cover Media Frame
        coverMediaFrame = ctk.CTkFrame(embedPageContent)
        

        coverMedia_label = ctk.CTkLabel(embedPageContent, text='Cover Media', font=customtkinter.CTkFont(family='Calibri', size=30))
        coverMedia_label.pack()

        #Audio upload placeholder
        audioUpload_label = ctk.CTkLabel(coverMediaFrame, text='Upload Audio', font=('Calibri', 20)) # , borderwidth=8, relief='solid' - figure our how to use in ctk
        audioUpload_label.pack(pady=10)

        #audioFile frame placeholder
        audioFileFrame = ctk.CTkFrame(master=coverMediaFrame) #frame

        audioFile_label = ctk.CTkLabel(master=audioFileFrame, width=30) #File display placeholder -- these: borderwidth=8, relief='solid' - figure our how to use in ctk
        deleteButton = ctk.CTkButton(master=audioFileFrame, text='x', width=3) #Trash icon button placeholder

        #Calling 
        audioFile_label.pack(side='left')
        deleteButton.pack(side='left')
        audioFileFrame.pack()
        #Cover frame
        coverMediaFrame.pack(side='left')

        #Hidden Data Frame
        hiddenDataFrame = ctk.CTkFrame(master=embedPageContent)

        hiddenData_label = ctk.CTkLabel(master=hiddenDataFrame, text='Hidden Data',font=('Calibri', 30))
        #Input field
        input = ctk.CTkEntry(master=hiddenDataFrame)
        inputString = ctk.StringVar()
        input = ctk.CTkEntry(master=hiddenDataFrame, textvariable=inputString) # , borderwidth=8, relief='solid'

        #or
        orLabel = ctk.CTkLabel(master=hiddenDataFrame, text='Or', font=('Calibri', 20))

        #File upload placeholder
        fileUpload_label = ctk.CTkLabel(master=hiddenDataFrame, text='Upload File', font=('Calibri', 20)) # , borderwidth=8, relief='solid'

        #Calling
        hiddenData_label.pack()
        input.pack()
        orLabel.pack()
        fileUpload_label.pack()

        #File frame placeholder
        fileFrame = ctk.CTkFrame(master=hiddenDataFrame) #frame

        file_label = ctk.CTkLabel(master=fileFrame, width=30 ) #File display placeholder -- , borderwidth=8, relief='solid'
        deleteButton = ctk.CTkButton(master=fileFrame, text='x', width=3) #Trash icon button placeholder

        #Calling 
        file_label.pack(side='left')
        deleteButton.pack(side='left')
        fileFrame.pack(pady=10)

        hiddenDataFrame.pack(side='left')

        
        #back_button = ctk.CTkButton(embedPage, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        #back_button.pack(pady=10)




# this is the code you had before, most of it is the same, but I've left this version here incase you want to look over it to see what the differences are! The main alteration is that it's been moved into a class.

''' #Inside window - we can probs inherit this and just have the contents later on !!So this would actually be a frame then? !!
window = tk.Tk()
window.title('Embed')
window.geometry('800x800') #Size of the window

#Cover Media Frame
coverMediaFrame = ttk.Frame(master=window)

coverMedia_label = ttk.Label(master=coverMediaFrame, text='Cover Media', font = 'Calibri 30')
coverMedia_label.pack()

#Audio upload placeholder
audioUpload_label = tk.Label(master=coverMediaFrame, text='Upload Audio', borderwidth=8, relief='solid', font='Calibri 20')
audioUpload_label.pack(pady=10)



#audioFile frame placeholder
audioFileFrame = ttk.Frame(master=coverMediaFrame) #frame

audioFile_label = tk.Label(master=audioFileFrame, width=30, borderwidth=8, relief='solid') #File display placeholder
deleteButton = ttk.Button(master=audioFileFrame, text='x', width=3) #Trash icon button placeholder

#Calling 
audioFile_label.pack(side='left')
deleteButton.pack(side='left')
audioFileFrame.pack()
#Cover frame
coverMediaFrame.pack(side='left')


#Hidden Data Frame
hiddenDataFrame = ttk.Frame(master=window)

hiddenData_label = ttk.Label(master=hiddenDataFrame, text='Hidden Data',font = 'Calibri 30')
#Input field
input = ttk.Entry(master=hiddenDataFrame)
inputString =tk.StringVar()
input = tk.Entry(master=hiddenDataFrame, textvariable=inputString, borderwidth=8, relief='solid')

#or
orLabel = tk.Label(master=hiddenDataFrame, text='Or', font='Calibri 20')

#File upload placeholder
fileUpload_label = tk.Label(master=hiddenDataFrame, text='Upload File', borderwidth=8, relief='solid', font='Calibri 20')

#Calling
hiddenData_label.pack()
input.pack()
orLabel.pack()
fileUpload_label.pack()

#File frame placeholder
fileFrame = ttk.Frame(master=hiddenDataFrame) #frame

file_label = tk.Label(master=fileFrame, width=30, borderwidth=8, relief='solid') #File display placeholder
deleteButton = ttk.Button(master=fileFrame, text='x', width=3) #Trash icon button placeholder

#Calling 
file_label.pack(side='left')
deleteButton.pack(side='left')
fileFrame.pack(pady=10)

hiddenDataFrame.pack(side='left')


#run
window.mainloop()
'''