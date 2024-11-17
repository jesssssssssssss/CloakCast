import customtkinter as ctk
import customtkinter
from PIL import Image
import os 
from os import system
from tkinter import filedialog
from stepic import encode, decode
from eyed3 import load
from PIL import Image
from tkinter import messagebox
import tkinter as tk
from encryption_utils import EncryptionUtils

class Sidebar(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#393839")
        self.controller=controller
        self.menuExpanded=False
        self.collapsedWidth=100
        self.expandedWidth=275

        self.menuExpanded = controller.sidebarExpanded

        self.configure(width=self.collapsedWidth)

        self.grid_rowconfigure(0, weight=0)  # Logo row
        self.grid_rowconfigure(1, weight=0)  # Menu icon row
        self.grid_rowconfigure(2, weight=1)  # Remaining space

        self.grid_columnconfigure(0, weight=1)
        self.grid_propagate(False)

        #Logo changes:
        # Get the current directory of this script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Define the relative path to the image
        logoPath = os.path.join(current_dir, "Images", "Logo.png")
        # Create the CTkImage with the correct image path
        self.logo = ctk.CTkImage(light_image=Image.open(logoPath), size=(80, 80))
        # Create a label for the logo
        self.logoLabel = ctk.CTkLabel(self, image=self.logo, text="")
        self.logoLabel.grid(row=0, column=0, padx=10, pady=(20, 0), sticky="nw")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        menuIconPath = os.path.join(current_dir, "Images", "HamburgerMenuIcon.png")

        self.menuIcon = ctk.CTkImage(light_image=Image.open(menuIconPath), size=(40,40))
        self.menuIconButton = ctk.CTkButton(
            self, 
            image=self.menuIcon, 
            text="", 
            fg_color="transparent", 
            hover_color="#2d2d2d",
            width=40, 
            height=40,  
            command=self.toggleMenu)
        self.menuIconButton.grid(row=1, column=0,  pady=(0, 20))
        

        # Menu Frame (initially hidden)
        self.menuFrame = ctk.CTkFrame(self, fg_color="#393839", corner_radius=8)

    def toggleMenu(self):
        if not self.menuExpanded:
            self.configure(width = self.expandedWidth)

            self.logoLabel.grid(row=0, column=0, padx=10, pady=(50, 30), sticky="n")

            self.menuFrame.grid(row=1, column=0, padx=20, pady=(70, 5), sticky="new")
            self.menuFrame.grid_columnconfigure(0, weight=1)  

            # About button
            aboutButton = ctk.CTkButton(            
                self.menuFrame, 
                text="How To Use", 
                command=lambda: self.controller.show_frame(HowToUsePage),
                text_color='#a63a50',
                fg_color='transparent',
                hover_color="#393839",  
                corner_radius=10,
                anchor="center",  
                width=200,  
                height=40,  
                font=("Lalezar", 26)  
            )
            aboutButton.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

            helpContactButton = ctk.CTkButton(            
                self.menuFrame, 
                text="Help / Contact Us", 
                command=lambda: self.controller.show_frame(HelpContactPage),
                text_color='#a63a50',
                fg_color='transparent',
                hover_color="#393839",  # change hover colour soon 
                corner_radius=10,
                anchor="center",  
                width=200,  
                height=40,  
                font=("Lalezar", 26)  
            )
            helpContactButton.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        else:
            self.collapse_menu()
        
        self.menuExpanded = not self.menuExpanded
        # Updating the MainApps state
        self.controller.sidebarExpanded = self.menuExpanded
    
    def collapse_menu(self):
        # Method specifically for collapsing the menu in page transitions
        self.configure(width=self.collapsedWidth)
        self.menuFrame.grid_forget()
        self.menuExpanded = False
        self.controller.sidebarExpanded = False

class BasePage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#FEFCFB")
        self.controller = controller
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Content frame wrapper (for centering the content frame)
        contentWrapper = ctk.CTkFrame(self, fg_color="transparent")
        contentWrapper.grid(row=0, column=1, sticky="nsew")
        contentWrapper.grid_columnconfigure(0, weight=1)
        contentWrapper.grid_rowconfigure(0, weight=1)

        # Outer content frame (for outer border)
        outerContentFrame = ctk.CTkFrame(contentWrapper, fg_color="#FEFCFB", corner_radius=10)
        outerContentFrame.grid(row=0, column=0, padx=20, pady=20)
        outerContentFrame.grid_columnconfigure(1, weight=1)
        outerContentFrame.grid_rowconfigure(1, weight=1)

        # Outer borders
        outerBottomBorder = ctk.CTkFrame(outerContentFrame, fg_color="#F2E2E5", height=5)
        outerBottomBorder.grid(row=2, column=0, columnspan=3, sticky="ew")

        # Content frame 
        self.contentFrame = ctk.CTkFrame(outerContentFrame, fg_color="#FEFCFB", corner_radius=10)
        self.contentFrame.grid(row=1, column=1, sticky="nsew")
        self.contentFrame.grid_columnconfigure(1, weight=1)
        self.contentFrame.grid_rowconfigure(1, weight=1)

        # Setting a fixed size for the content frame here
        self.contentFrame.configure(width=800, height=600)
        self.contentFrame.grid_propagate(False)  # This prevents the frame from shrinking

        innerBottomBorder = ctk.CTkFrame(self.contentFrame, fg_color="#E6C7CC", height=8)
        innerBottomBorder.grid(row=2, column=0, columnspan=3, sticky="ew")

        innerLeftBorder = ctk.CTkFrame(self.contentFrame, fg_color="#E6C7CC", width=3)
        innerLeftBorder.grid(row=0, column=0, rowspan=3, sticky="ns")

        innerRightBorder = ctk.CTkFrame(self.contentFrame, fg_color="#E6C7CC", width=3)
        innerRightBorder.grid(row=0, column=2, rowspan=3, sticky="ns")

        # ********************* !!!!!!!!!!!!!!!!!! ------------------------------
        
        self.create_content()
        
        self.sidebar = Sidebar(self, controller)
        self.sidebar.place(x=0, y=0, relheight=1.0)

        def onShowFrame(self):
            pass
        
  
    
    def create_content(self):
        # Must be implemented by all child classes 
        raise NotImplementedError

class HomePage(BasePage):

    def create_content(self):

        # Home page content
        homePageContent = ctk.CTkFrame(self.contentFrame, fg_color='White', corner_radius=10)
        homePageContent.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        homePageContent.grid_columnconfigure((0, 1), weight=1)

# * ***********
        # CloakCast label
        label = ctk.CTkLabel(homePageContent, text="CloakCast", font=("Lalezar", 120), text_color="#a63a50", fg_color="white")
        label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)

        # Embed button
        embedButton = ctk.CTkButton(
            homePageContent, 
            text="Embed", 
            command=lambda: self.controller.show_frame(EmbedPage),
            text_color='White',
            fg_color='#393839',
            corner_radius=10,
            font=('Lalezar', 45), 
            width=160,  
            height=20)   
      
        embedButton.grid(row=1, column=0, padx=(100, 0), pady=(0, 15), ipadx=15, ipady=0)

        # Extract button
        extractButton = ctk.CTkButton(            
            homePageContent, 
            text="Extract", 
            command=lambda: self.controller.show_frame(ExtractPage),
            text_color='White',
            fg_color='#393839',
            corner_radius=10,
            font=('Lalezar', 45),
            width=160,  
            height=20   
        )
        extractButton.grid(row=1, column=1, padx=(0, 100), pady=(0, 15), ipadx=15, ipady=0)

        hpTextFrame = ctk.CTkFrame(
            homePageContent,
            fg_color="#2d2d2d",
            corner_radius=8
        )
        hpTextFrame.grid(row=2, column=0, padx=100, pady=40, columnspan=2)


        hpScrollBox = ctk.CTkTextbox(
            hpTextFrame,
            width=485,
            height=200,
            fg_color="white",
            text_color="black",
            corner_radius=8,
            font=("Arial", 16),
            wrap="word"  
        )
        hpScrollBox.grid(row=0, column=0, padx=15, pady=15)
        hpScrollBox.insert("1.0", "How this works Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sit amet odio ullamcorper, dictum libero non, facilisis magna. Fusce id pulvinar neque, ut pretium odio. Nunc finibus ante nec massa dictum vestibulum. Etiam id consequat purus, quis dapibus est.Aliquam viverra vitae lectus in vehicula. In ac diam ac justo tincidunt efficitur.")

class EmbedPage(BasePage):

    def onShowFrame(self):
        # This method will be called whenever the page is shown
        self.resetPage()
        
    def resetPage(self):

        if hasattr(self, 'selectedAudioFile'):  # Checking first if attributes exist
            self.selectedAudioFile.set("No File Selected") # Resetting the attributes
        if hasattr(self, 'dataInput'):
            self.dataInput.delete(0, 'end')
        if hasattr(self, 'inputAccessCode'):
            self.inputAccessCode.delete(0, 'end')
        if hasattr(self, 'ConfirmAccessCode'):
            self.ConfirmAccessCode.delete(0, 'end')
        if hasattr(self, 'statusLabel'):
            self.statusLabel.configure(text="")
        if hasattr(self, 'selectedTextFile'):
            self.selectedTextFile.set("No File Selected")

    def create_content(self):

        #Functions--------------------

        #Variable holding selected audio file and text file
        self.selectedAudioFile = ctk.StringVar(value="No File Selected")
        self.selectedTextFile = ctk.StringVar(value="No File Selected")

        #Function to browse and open audio file
        def openAudioFile():
          filePath = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
          if filePath:
           #Chosen audio display
            self.selectedAudioFile.set(filePath) #updates the selected audio file
            print(f"Selected file: {filePath}")
        
        def openTextFile():
            filePath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            if filePath:
                self.selectedTextFile.set(filePath) #updates the selected text file
                print(f"Selected text file: {filePath}")
 
        #Function to delete selected audio file
        def deleteAudio():
            self.selectedAudioFile.set("No File Selected")
            deleteButton.configure(state=ctk.NORMAL) #Active only when a file has been selected

        def encoder():
            #Setting data for exception handling
            data = "No File Selected"

            #Getting hidden data, file path and access code
            data = dataInput.get().strip()
            textFilePath = self.selectedTextFile.get()
            accessCode = inputAccessCode.get()
            confirmCode = ConfirmAccessCode.get()
            
            #Validating access codes matching
            if accessCode != confirmCode:
                self.statusLabel.configure(text="Access codes do not match!", text_color='#a63a50')
                return False #Returning false if codes don't match
            
            #Checking if both data has been inptuted and a file has been selected
            if data and textFilePath != "No File Selected":
                self.statusLabel.configure(text=f"You can not embed a message and a file. Please choose one", text_color='#a63a50')
                return False
            
            #Checking if neither input data or a file has been selected
            if not data and textFilePath == "No File Selected":
                self.statusLabel.configure(text=f"Please enter a Message or Upload a File", text_color='#a63a50')
                return False
            
            #Checking if a file has been selected and it exists
            if not data: # and self.selectedAudioFile - add this later
                try:
                    #Reading data from the selected text file
                    with open(textFilePath, "r") as file: #the 'with' ensures the file closes when finished reading
                            data = file.read()

                except Exception as e:
                        self.statusLabel.configure(text="Failed to read file: {str(e)}", text_color='#a63a50')
                        return False
            try:         

                # Encrypting the data here
                encryptedData = EncryptionUtils.encrypt_data(data, accessCode) 
                
                #Getting chosen audio file
                audioPath = self.selectedAudioFile.get()
                #Error message for when required data has not been entered
                if audioPath == "No File Selected":
                    self.statusLabel.configure(text="Please select a Cover Media", text_color='#A63A50')
                    return False

                imgName = 'smile.png'
                audio = load(audioPath) #Opens the audio

                #Opens the image and puts the encrypted data inside saves it
                img = Image.open(imgName)
                imgStegano = encode(img, encryptedData) 
                imgStegano.save(imgName)

                #Making the image the cover of the audio
                audio.initTag()
                audio.tag.images.set(3, open(imgName, "rb").read(), "image/png")
                audio.tag.save()

                return True # Returns true if successful 
            except Exception as e:
                self.statusLabel.configure(text=f"Failed to encrypt and embed data: {str(e)}", text_color='#a63a50')
                return False #Returns false if there is an error

        def submitAction():
            #Checks if encoder was successful and then opens success page
            if encoder(): 
                self.controller.show_frame(EmbedSuccessPage) 

        #Content--------------------

        embedPageContent = ctk.CTkFrame(self.contentFrame, fg_color='White', corner_radius=10) 
        embedPageContent.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        embedPageContent.grid_columnconfigure((0,1), weight=1)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        backArrowPath = os.path.join(current_dir, "Images", "BackArrow.png")

        self.backArrow = ctk.CTkImage(light_image=Image.open(backArrowPath), size=(40,40))
        self.backArrowButton = ctk.CTkButton(
            embedPageContent, 
            image=self.backArrow, 
            text="", 
            fg_color="transparent",
            width=50,
            command=lambda: self.controller.show_frame(HomePage))
        self.backArrowButton.grid(row=0, column=0, padx=(0,0), ipadx=0, ipady=0, sticky='w')

        #Cover Media--------------------
 
        coverMediaLabel = ctk.CTkLabel(master=embedPageContent, text='Cover Media', text_color='#a63a50', font=('lalezar', 40))
        coverMediaLabel.grid(row=1, column=0, padx=(40,0))
        
        #Audio upload button
        audioUploadButton = ctk.CTkButton(master=embedPageContent,
                                    text='Upload Audio',
                                    text_color='#393839',
                                    border_width= 7,
                                    border_color='#393839',
                                    corner_radius = 100,
                                    fg_color= '#FFFFFF',
                                    font=('Lalezar', 24),
                                    command=openAudioFile,
                                    height=50) 
        audioUploadButton.grid(row=2, column=0, pady=(10, 0), padx=(40,0))
        
        audioFileLabelFrame = ctk.CTkFrame(
            embedPageContent,
            fg_color="#393839",
            corner_radius=100,
        )
        audioFileLabelFrame.grid(row=3, column=0, pady=0, padx=(40,0))

        #Chosen audio display, uses selectedAudioFile
        audioFileLabel = ctk.CTkLabel(master=audioFileLabelFrame,
                                    textvariable= self.selectedAudioFile,
                                    corner_radius = 100,
                                    height=35,
                                    width=260,
                                    fg_color= '#FFFFFF',
                                    text_color="#393839")
        audioFileLabel.grid(row=0, column=0, padx=10, pady=6)

        #Delete button for chosen audio file display
        deleteButton = ctk.CTkButton(master=audioFileLabel, text='x', height=0.5, width=1, hover_color="#FFFFFF", text_color="#a63a50", fg_color="#FFFFFF", command= deleteAudio, font=("Sniglet", 22)) #Trash icon button placeholder
        deleteButton.grid(row=0, column=0, sticky='e', padx=(0,20), pady=(0,3))
        
        #Access Code--------------------
        
        #Header
        accessCodeLabel = ctk.CTkLabel(master=embedPageContent, text='Access Code', text_color='#a63a50', font=('lalezar', 40))
        accessCodeLabel.grid(row=4, column=0, padx=(40,0))
        
        enterCodeLabel = ctk.CTkLabel(master=embedPageContent, text='Enter Code', text_color='#393839', font=('lalezar', 20))
        enterCodeLabel.grid(row=5, column=0, padx=(40,0))
        
        inputAccessCodeFrame = ctk.CTkFrame(
            embedPageContent,
            fg_color="#393839",
            corner_radius=100,
            
        )
        inputAccessCodeFrame.grid(row=6, column=0, padx=(40,0))

        #Input field

        inputAccessCode = ctk.CTkEntry(master=inputAccessCodeFrame, placeholder_text='...', placeholder_text_color='#393839', fg_color="white", corner_radius=100, width=180, height=28)
        inputAccessCode.grid(row=6, column=0, padx=5, pady=5)
        
        #View access code button
        viewAccessCode = ctk.CTkButton(master=embedPageContent, text='o', width=3) #eye icon button placeholder
        viewAccessCode.grid(row=6, column=1)
        
        confirmCodeLabel = ctk.CTkLabel(master=embedPageContent, text='Confirm Code', width=50, text_color='#393839', font=('lalezar', 20))
        confirmCodeLabel.grid(row=7, column=0, padx=(40,0))
        
        #Confirm input field

        ConfirmAccessCodeFrame = ctk.CTkFrame(
            embedPageContent,
            fg_color="#393839",
            corner_radius=100,
            
        )
        ConfirmAccessCodeFrame.grid(row=8, column=0, padx=(40,0))

        ConfirmAccessCode = ctk.CTkEntry(master=ConfirmAccessCodeFrame, placeholder_text='...', placeholder_text_color='#393839', fg_color="white", corner_radius=100, width=180, height=28)
        ConfirmAccessCode.grid(row=6, column=0, padx=5, pady=5)
        
        #View confirmed access code button
        viewConfirmedAccessCode = ctk.CTkButton(master=embedPageContent, text='-', width=3) #eye icon button placeholder
        viewConfirmedAccessCode.grid(row=8, column=1)
        
        
        #Hidden Data--------------------
        
        hiddenDataLabel = ctk.CTkLabel(master=embedPageContent, text='Hidden Data', text_color='#a63a50', font=('Lalezar', 40))
        hiddenDataLabel.grid(row=1, column=3, padx=(0,50))
        

        dataInputFrame = ctk.CTkFrame(
            embedPageContent,
            fg_color="#393839",
            corner_radius=10,
            
        )
        dataInputFrame.grid(row=2, column=3, rowspan=2, padx=(0,50))

        #Input field
        dataInput = ctk.CTkEntry(master=dataInputFrame, placeholder_text='Enter Message...', placeholder_text_color='#393839', font=('Sniglet', 20), fg_color="white", width=230, height=130)
        dataInput.grid(row=2, column=3, padx=5, pady=5, rowspan=2)
        
        #or
        orLabel = ctk.CTkLabel(master=embedPageContent, text='or', font=('Sniglet', 24), text_color="#a63a50")
        orLabel.grid(row=4, column=3, padx=(0,50))
        
        #Text file upload button
        fileUploadButton = ctk.CTkButton(master=embedPageContent,
                                    text='Upload File',
                                    text_color='#a63a50',
                                    border_width= 3,
                                    border_color='#393839',
                                    corner_radius = 10,
                                    fg_color= '#FFFFFF',
                                    font=('Lalezar', 30),
                                    command=openTextFile) 
        fileUploadButton.grid(row=5, column=3, pady=20, padx=(0,50))
        
        #Chosen text file display placeholder
        fileUploadLabel = ctk.CTkLabel(master=embedPageContent,
                                    textvariable=self.selectedTextFile,
                                    fg_color= 'red',
                                    corner_radius = 10) #File display placeholder
        fileUploadLabel.grid(row=6, column=3)
        
        #Delete button for chosen Text file display
        deleteButton = ctk.CTkButton(master=embedPageContent, text='x', width=3) #Trash icon button placeholder
        deleteButton.grid(row=6, column=4)

        #Submit button--------------------
        submitButton = ctk.CTkButton(master=embedPageContent,
                                    text='Submit',
                                    text_color='#FFFFFF',
                                    corner_radius = 10,
                                    fg_color= '#a63a50',
                                    font=('Lalezar', 30),
                                    command = submitAction)
        submitButton.grid(row=8,column=2)

        self.statusLabel = ctk.CTkLabel(
            master=embedPageContent,
            text="", 
            text_color='#393839',
            font=('Lalezar', 16)
        )
        self.statusLabel.grid(row=9, column=2, pady=(10,0)) 

class EmbedSuccessPage(BasePage):
 
    def create_content(self):
 
        embedSuccessContent = ctk.CTkFrame(self.contentFrame, fg_color='White', corner_radius=10)
        embedSuccessContent.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        embedSuccessContent.grid_columnconfigure((0, 1), weight=1)
 
        #Functions
 
        #returns user back to home page on click
        def returnAction():
            self.controller.show_frame(HomePage)
 
        #Audio embedded success label
        embedSuccessLabel = ctk.CTkLabel(master=embedSuccessContent,
                                    text='Audio Embedded Successfully!',
                                    text_color= '#a63a50',
                                    font=('Lalezar', 30),
                                    corner_radius = 10)
        embedSuccessLabel.grid(row=0, column=0, padx=(130,0), pady=(200,0))
 
        #Button to return to home page
        returnHomeButton = ctk.CTkButton(master=embedSuccessContent,
                                         text='Return Home',
                                         text_color='#FFFFFF',
                                         corner_radius = 10,
                                         fg_color= '#a63a50',
                                         font=('Lalezar', 30),
                                         command= returnAction)
        returnHomeButton.grid(row=1, column=0, padx=(130,0))
 
        #Displaying audio file path
        #audioFileLabel = ctk.CTkLabel(master=self,
         #                           text= ,
          #                          corner_radius = 10,
          #                          fg_color= '#000000')
        #audioFileLabel.grid(row=1, column=0, columnspan=2, padx=20, pady=(10, 20), sticky="ew")
        
class ExtractPage(BasePage):
 

    def onShowFrame(self):
           
           self.resetPage()
        
    def resetPage(self):
      
        if hasattr(self, 'selectedAudioFile'):
            self.selectedAudioFile.set("No File Selected")
        if hasattr(self, 'accessCodeInput'):
            self.accessCodeInput.delete(0, 'end')
        if hasattr(self, 'resultText'):
            self.resultText.delete(1.0, tk.END)
        if hasattr(self, 'statusLabel'):
            self.statusLabel.configure(text="")

    def create_content(self):
 
        #Functions--------------------
 
        #Variable holding selected audio file
        self.selectedAudioFile = ctk.StringVar(value="No File Selected")
 
        #Function to browse and open audio file
        def openAudioFile():
          filePath = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
          if filePath:
           #Chosen audio display
            self.selectedAudioFile.set(filePath) #updates the string
            print(f"Selected file: {filePath}")
 
        #Function to delete selected audio file
        def deleteAudio():
            selectedAudioFile = set("No File Selected")
            deleteButton.configure(state=ctk.NORMAL) #Active only when a file has been selected

        def decoder():
            try:
                # Getting the access code
                accessCode = accessCodeInput.get()
                
                #Audio to be extracted is chosen and loaded
                audioPath = self.selectedAudioFile.get()
                audio = load(audioPath)

                #Creating an image to save the encrypted data to, from the cover of the song
                img = open("tempImg.png", "wb")
                img.write(audio.tag.images[0].image_data)
                img.close()

                #The secret text is save in the temp image
                img = Image.open("tempImg.png")
                encryptedData = decode(img)
                system("del tempImg.png")  # Deleting the temp image
                
                # Decrypting the data
                decrypted_data = EncryptionUtils.decrypt_data(encryptedData, accessCode)
                
                # Showing the decrypted data to user
                resultText.delete(1.0, tk.END)  # Clear previous content
                resultText.insert(tk.END, decrypted_data)
                self.statusLabel.configure(text="Data extracted and decrypted successfully!", text_color='#28a745')
                
            except Exception as e:
                self.statusLabel.configure(text=f"Failed to extract and decrypt data: {str(e)}", text_color='#a63a50')

 
        def extractAction():
            decoder() #Running the decoder function when clicked
 
        # Extract page content
        extractPageContent = ctk.CTkFrame(self.contentFrame, fg_color='White', corner_radius=10)
        extractPageContent.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        extractPageContent.grid_columnconfigure((0, 1), weight=1)

        # Back arrow that returns user to home
        current_dir = os.path.dirname(os.path.abspath(__file__))
        backArrowPath = os.path.join(current_dir, "Images", "BackArrow.png")
 
        self.backArrow = ctk.CTkImage(light_image=Image.open(backArrowPath), size=(40,40))
        self.backArrowButton = ctk.CTkButton(
            extractPageContent,
            image=self.backArrow,
            text="",
            fg_color="transparent",
            command=lambda: self.controller.show_frame(HomePage))
        self.backArrowButton.grid(row=0, column=0, padx=(0,0), ipadx=0, ipady=0)
 
 
        #Audio upload button
        audioUploadButton = ctk.CTkButton(
            extractPageContent,
            text="Upload File",
            command=openAudioFile,
            text_color='White',
            fg_color='#393839',
            corner_radius=100,
            font=('Lalezar', 30))
        audioUploadButton.grid(row=3, column=1, padx=(0,260), pady=(100,20))
 
 
        #Chosen audio display
        audioFileLabel = ctk.CTkLabel(master=extractPageContent,
                                    textvariable= self.selectedAudioFile,
                                    fg_color= '#FFFFFF',
                                    corner_radius = 10)
        audioFileLabel.grid(row=4, column=1, padx=(0,260), pady=(50,0))

                # Access Code input
        accessCodeLabel = ctk.CTkLabel(master=extractPageContent, 
                                    text='Access Code', 
                                    text_color='#393839', 
                                    font=('lalezar', 20))
        accessCodeLabel.grid(row=5, column=1, padx=(0,260), pady=(20,0))

        accessCodeFrame = ctk.CTkFrame(
            extractPageContent,
            fg_color="#393839",
            corner_radius=100,
        )
        accessCodeFrame.grid(row=6, column=1, padx=(0,260))

        accessCodeInput = ctk.CTkEntry(
            master=accessCodeFrame, 
            placeholder_text='Enter access code...', 
            placeholder_text_color='#393839',
            fg_color="white",
            corner_radius=100,
            width=180,
            height=28,
            show="*"  # This will hide the password
        )
        accessCodeInput.grid(row=0, column=0, padx=5, pady=5)

        # Result text area
        resultText = ctk.CTkTextbox(
            master=extractPageContent,
            width=300,
            height=100,
            corner_radius=10
        )
        resultText.grid(row=8, column=1, padx=(0,260), pady=(20,0))
 
        #Extract button--------------------
        extractButton = ctk.CTkButton(master=extractPageContent,
                                    text='Extract',
                                    text_color='#FFFFFF',
                                    corner_radius = 10,
                                    fg_color= '#a63a50',
                                    font=('Lalezar', 30),
                                    command = extractAction)
        extractButton.grid(row=7,column=1, padx=(0,260), pady=(90,0))

        self.statusLabel = ctk.CTkLabel(
            master=extractPageContent,
            text="",  # Empty by default
            text_color='#393839',
            font=('Lalezar', 16)
        )
        self.statusLabel.grid(row=9, column=1, padx=(0,260), pady=(10,0))

class HowToUsePage(BasePage):

    def create_content(self):

        htuPageContent = ctk.CTkFrame(self.contentFrame, fg_color='White', corner_radius=10)
        htuPageContent.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        htuPageContent.grid_columnconfigure((0, 1), weight=1)

        # Back arrow that returns user to home
        current_dir = os.path.dirname(os.path.abspath(__file__))
        backArrowPath = os.path.join(current_dir, "Images", "BackArrow.png")

        self.backArrow = ctk.CTkImage(light_image=Image.open(backArrowPath), size=(40,40))
        self.backArrowButton = ctk.CTkButton(
            htuPageContent, 
            image=self.backArrow, 
            text="", 
            fg_color="transparent",
            command=lambda: (
                self.sidebar.collapse_menu(),
                self.controller.show_frame(HomePage)
            )
        )
        
        self.backArrowButton.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nw")
        
        headLabel = ctk.CTkLabel(
            master=htuPageContent, 
            text='How To Use CloakCast', 
            text_color="#A63A50",
            font=('Sniglet', 50)
        )
        headLabel.grid(row=0, column=0, columnspan=2, pady=(20, 5), sticky="n")  

        # terms and definitions 

        coverMediaLabel = ctk.CTkLabel(
            htuPageContent,
            text="Cover Media",
            font=('Lalezar', 24),
            text_color="#A63A50",
            justify="right"
        )
        coverMediaLabel.grid(row=1, column=0, padx=(40, 20), pady=20, sticky="e")

        coverMediaDefFrame = ctk.CTkFrame(
            htuPageContent,
            fg_color="#2d2d2d",
            corner_radius=10
        )
        coverMediaDefFrame.grid(row=1, column=1, padx=(20, 40), pady=5, sticky="w")

        coverMediaDef = ctk.CTkTextbox(
            coverMediaDefFrame,
            height=60,
            width=400,
            fg_color="white",
            text_color="black",
            corner_radius=10,
            font=("Arial", 16)
        )
        coverMediaDef.grid(row=0, column=0, padx=10, pady=6)
        coverMediaDef.insert("1.0", "This is the audio that you would like to hide your\nmessage, or data, inside of.")
        coverMediaDef.configure(state="disabled") 

        
        hiddenDataLabel = ctk.CTkLabel(
            htuPageContent,
            text="Hidden Data",
            font=('Lalezar', 24),
            text_color="#A63A50",
            justify="right"
        )
        hiddenDataLabel.grid(row=2, column=0, padx=(40, 20), pady=20, sticky="e")

        hiddenDataDefFrame = ctk.CTkFrame(
            htuPageContent,
            fg_color="#2d2d2d",
            corner_radius=10
        )
        hiddenDataDefFrame.grid(row=2, column=1, padx=(20, 40), pady=5, sticky="w")

        hiddenDataDef = ctk.CTkTextbox(
            hiddenDataDefFrame,
            height=60,
            width=400,
            fg_color="white",
            text_color="black",
            corner_radius=8,
            font=("Arial", 16)
        )
        hiddenDataDef.grid(row=0, column=0, padx=10, pady=6)
        hiddenDataDef.insert("1.0", "The ‘Hidden Data’ is the message that you would like\nto hide, or cover, with an audio.")
        hiddenDataDef.configure(state="disabled")

              
        accessCodeLabel = ctk.CTkLabel(
            htuPageContent,
            text="Access Code",
            font=('Lalezar', 24),
            text_color="#A63A50",
            justify="right"
        )
        accessCodeLabel.grid(row=3, column=0, padx=(40, 20), pady=20, sticky="e")

        accessCodeDefFrame = ctk.CTkFrame(
            htuPageContent,
            fg_color="#2d2d2d",
            corner_radius=10
        )
        accessCodeDefFrame.grid(row=3, column=1, padx=(20, 40), pady=5, sticky="w")

        accessCodeDef = ctk.CTkTextbox(
            accessCodeDefFrame,
            height=80,
            width=400,
            fg_color="white",
            text_color="black",
            corner_radius=8,
            font=("Arial", 16)
        )
        accessCodeDef.grid(row=0, column=0, padx=10, pady=6)
        accessCodeDef.insert("1.0", "You can add an access code to further secure your \ndata. This acts as a password that will need to be \nentered before your file can be extracted.")
        accessCodeDef.configure(state="disabled")

        embedLabel = ctk.CTkLabel(
            htuPageContent,
            text="Embed",
            font=('Lalezar', 24),
            text_color="#A63A50",
            justify="right"
        )
        embedLabel.grid(row=4, column=0, padx=(40, 20), pady=20, sticky="e")

        embedDefFrame = ctk.CTkFrame(
            htuPageContent,
            fg_color="#2d2d2d",
            corner_radius=10
        )
        embedDefFrame.grid(row=4, column=1, padx=(20, 40), pady=5, sticky="w")

        embedDef = ctk.CTkTextbox(
            embedDefFrame,
            height=93,
            width=400,
            fg_color="white",
            text_color="black",
            corner_radius=8,
            font=("Arial", 16)
        )
        embedDef.grid(row=0, column=0, padx=10, pady=6)
        embedDef.insert("1.0", "Once inputting the required information on the Embed page, simply click the ‘Embed Audio’ button. This will \ntake you to a page where you can download your \nhidden data.")
        embedDef.configure(state="disabled")

        extractLabel = ctk.CTkLabel(
            htuPageContent,
            text="Extract",
            font=('Lalezar', 24),
            text_color="#A63A50",
            justify="right"
        )
        extractLabel.grid(row=5, column=0, padx=(40, 20), pady=20, sticky="e")

        extractDefFrame = ctk.CTkFrame(
            htuPageContent,
            fg_color="#2d2d2d",
            corner_radius=10
        )
        extractDefFrame.grid(row=5, column=1, padx=(20, 40), pady=20, sticky="w")

        extractDef = ctk.CTkTextbox(
            extractDefFrame,
            height=60,
            width=400,
            fg_color="white",
            text_color="black",
            corner_radius=8,
            font=("Arial", 16)
        )
        extractDef.grid(row=0, column=0, padx=10, pady=6)
        extractDef.insert("1.0", "After uploading the embedded file, select the ‘Extract’ button to view the hidden data.")
        extractDef.configure(state="disabled")

class HelpContactPage(BasePage):
    def create_content(self):

        helpContactPageContent = ctk.CTkFrame(self.contentFrame, fg_color='White', corner_radius=10)
        helpContactPageContent.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        helpContactPageContent.grid_columnconfigure((0, 1), weight=1)

        # Back arrow that returns user to home
        current_dir = os.path.dirname(os.path.abspath(__file__))
        backArrowPath = os.path.join(current_dir, "Images", "BackArrow.png")

        self.backArrow = ctk.CTkImage(light_image=Image.open(backArrowPath), size=(40,40))
        self.backArrowButton = ctk.CTkButton(
            helpContactPageContent, 
            image=self.backArrow, 
            text="", 
            fg_color="transparent",
            command=lambda: (
                self.sidebar.collapse_menu(),
                self.controller.show_frame(HomePage)
            )
        )
        
        self.backArrowButton.grid(row=0, column=0, padx=(0,0), ipadx=0, ipady=0)
        
        headLabel = ctk.CTkLabel(master=helpContactPageContent, text='Help / Contact Us', font=('Lalezar', 50))
        headLabel.grid(row=1, column=1, sticky="w")




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