import customtkinter as ctk
from customtkinter import CTkImage
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
from db_utils import DatabaseManager

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
        hpScrollBox.insert("1.0", "Welcome to CloakCast, your gateway to secure and seamless audio steganography. CloakCast allows you to discreetly embed messages or text files into an MP3 audio file of your choice. Navigate to the Embed page to upload your cover audio, set a unique access code, and select whether to embed a typed message or an uploaded text file. The modified audio file is saved directly to your computer, eliminating the need for additional downloads. Share your audio file with colleagues, who can retrieve the hidden data on the Extract page. For detailed guidance, visit the How To Use section.")

class EmbedPage(BasePage):

    def onShowFrame(self):
        # This method will be called whenever the page is shown
        self.resetPage()
        
    def resetPage(self):
        # Reset file selections
        if hasattr(self, 'selectedAudioFile'):
            self.selectedAudioFile.set("No File Selected")
        if hasattr(self, 'selectedTextFile'):
            self.selectedTextFile.set("No File Selected")
        
        # Reset input fields
        if hasattr(self, 'inputAccessCode'):
            self.inputAccessCode.delete(0, 'end')
        if hasattr(self, 'ConfirmAccessCode'):
            self.ConfirmAccessCode.delete(0, 'end')
        if hasattr(self, 'dataInput'):
            self.dataInput.delete(0, 'end')
        
        # Reset status label
        if hasattr(self, 'statusLabel'):
            self.statusLabel.configure(text="")
        
        # Remove file paths if they exist
        if hasattr(self, 'fullAudioPath'):
            delattr(self, 'fullAudioPath')
        if hasattr(self, 'fullTextPath'):
            delattr(self, 'fullTextPath')
        
        # Reset password visibility
        if hasattr(self, 'input_code_hidden'):
            self.input_code_hidden[0] = True
        if hasattr(self, 'confirm_code_hidden'):
            self.confirm_code_hidden[0] = True

    def create_content(self):

        #Functions--------------------

        #Variable holding selected audio file and text file
        self.selectedAudioFile = ctk.StringVar(value="No File Selected")
        self.selectedTextFile = ctk.StringVar(value="No File Selected")

        #Function to browse and open audio file
        def openAudioFile():
            filePath = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
            if filePath:
                # Getting just the filename from the full path
                fileName = os.path.basename(filePath)
                self.selectedAudioFile.set(fileName)  
                self.fullAudioPath = filePath  
                print(f"Selected file: {filePath}")

        #Function to browse and open text file
        def openTextFile():
            filePath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            if filePath:
                fileName = os.path.basename(filePath)
                self.selectedTextFile.set(fileName)  
                self.fullTextPath = filePath  
                print(f"Selected text file: {filePath}")
    
        #Function to delete selected audio file
        def deleteAudio():
            self.selectedAudioFile.set("No File Selected")
            if hasattr(self, 'fullAudioPath'):
                delattr(self, 'fullAudioPath')

        #Function to delete selected text file
        def deleteText():
            self.selectedTextFile.set("No File Selected")
            if hasattr(self, 'fullTextPath'):
                delattr(self, 'fullTextPath')

        #This function hides and shows entered access code
        def togglePassword(entry, button, hidden):
            if hidden[0]:  # If currently hidden
                entry.configure(show="")  # Show text
                button.configure(image=openEyeImage)  # Set open eye icon
            else:
                entry.configure(show="*")  # Hide text
                button.configure(image=hideEyeImage)  # Set hide eye icon
            hidden[0] = not hidden[0]  # Toggle the state
   
        def encoder():
            #Getting hidden data, file path and access code
            data = self.dataInput.get().strip()
            textFilePath = self.selectedTextFile.get()
            accessCode = self.inputAccessCode.get()
            confirmCode = self.ConfirmAccessCode.get()
            
            #Validating access codes matching
            if accessCode != confirmCode:
                messagebox.showerror("Error", "Access codes do not match!")
                return 
            
            #Checking if both data has been inptuted and a file has been selected
            if data and textFilePath != "No File Selected":
                messagebox.showerror("Error", "You can not embed a message and a file. Please choose one")
                return 
            
            #Checking if neither input data or a file has been selected
            if not data and textFilePath == "No File Selected":
                messagebox.showerror("Error", "Please enter a Message or Upload a File")
                return 
            
            #Checking if a file has been selected and it exists
            if not data:  # If using text file
                textFilePath = getattr(self, 'fullTextPath', None)
                if not textFilePath:
                    messagebox.showerror("Error", "Please select a text file")
                    return False
                try:
                    with open(textFilePath, "r") as file:
                        data = file.read()

                except Exception as e:
                        messagebox.showerror("Error", "Failed to read file: {str(e)}")
                        return 
            try:         

                # Encrypting the data here
                encryptedData = EncryptionUtils.encrypt_data(data, accessCode) 
                
                #Getting chosen audio file
                audioPath = getattr(self, 'fullAudioPath', None)
                #Error message for when required data has not been entered
                if not audioPath:
                    messagebox.showerror("Error", "Please select a Cover Media")
                    return False

                imgName = 'Images\\Cone.png'
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
                messagebox.showerror("Error", "Failed to encrypt and embed data: {str(e)}")
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
                                    text_color='#ffffff',
                                    border_color='#393839',
                                    corner_radius = 100,
                                    fg_color= '#393839',
                                    font=('Lalezar', 24),
                                    command=openAudioFile,
                                    height=40) 
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
        deleteButton = ctk.CTkButton(master=audioFileLabel, text='x', height=0.5, width=1, hover_color="#FFFFFF", text_color="#a63a50", fg_color="#FFFFFF", 
                                     command= deleteAudio, font=("Sniglet", 22)) 
        deleteButton.grid(row=0, column=0, sticky='e', padx=(0,20), pady=(0,3))
        
        #Access Code--------------------
        
        #Header
       
        accessCodeLabel = ctk.CTkLabel(master=embedPageContent, text='Access Code', text_color='#a63a50', font=('lalezar', 40))
        accessCodeLabel.grid(row=4, column=0, padx=(40,0), pady=(10,5))  # Reduced bottom padding

        enterCodeLabel = ctk.CTkLabel(master=embedPageContent, text='Enter Code', text_color='#393839', font=('lalezar', 20))
        enterCodeLabel.grid(row=5, column=0, padx=(40,0), pady=(0,5))  

        # Initialize the toggle state
        self.input_code_hidden = [True]
        self.confirm_code_hidden = [True]

        # Load and prepare the images
        hideEyeImage = ctk.CTkImage(
            light_image=Image.open("Images\\HideEye.png"),
            size=(10, 10) 
        )

        openEyeImage = ctk.CTkImage(
            light_image=Image.open("Images\\OpenEye.png"), 
            size=(10, 10)  
        )

        inputAccessCodeFrame = ctk.CTkFrame(
            embedPageContent,
            fg_color="#393839",
            corner_radius=100,
        )
        inputAccessCodeFrame.grid(row=6, column=0, padx=(40,0), pady=(0,10))  

        # Create input access code as a class attribute
        self.inputAccessCode = ctk.CTkEntry(
            master=inputAccessCodeFrame, 
            placeholder_text='...', 
            placeholder_text_color='#393839', 
            fg_color="white", 
            corner_radius=100, 
            width=180, 
            height=28, 
            show="*"
        )
        self.inputAccessCode.grid(row=0, column=0, padx=5, pady=5)

        # View access code button
        viewAccessCode = ctk.CTkButton(
            master=self.inputAccessCode, 
            image=hideEyeImage, 
            text="", 
            width=3, 
            height=3, 
            fg_color='#FFFFFF', 
            text_color='#393839', 
            hover_color='#FFFFFF',
            command=lambda: togglePassword(self.inputAccessCode, viewAccessCode, self.input_code_hidden)
        )
        viewAccessCode.grid(row=0, column=0, sticky='e', padx=(0, 10))
        
        confirmCodeLabel = ctk.CTkLabel(master=embedPageContent, text='Re-Enter Code', text_color='#393839', font=('lalezar', 20))
        confirmCodeLabel.grid(row=7, column=0, padx=(40,0), pady=(0,5)) 

        # Confirm Access Code section
        ConfirmAccessCodeFrame = ctk.CTkFrame(
            embedPageContent,
            fg_color="#393839",
            corner_radius=100,
        )
        ConfirmAccessCodeFrame.grid(row=8, column=0, padx=(40,0))

        self.ConfirmAccessCode = ctk.CTkEntry(
            master=ConfirmAccessCodeFrame, 
            placeholder_text='...', 
            placeholder_text_color='#393839', 
            fg_color="white", 
            corner_radius=100, 
            width=180, 
            height=28, 
            show="*"
        )
        self.ConfirmAccessCode.grid(row=0, column=0, padx=5, pady=5)
        
        # View confirmed access code button
        viewConfirmedAccessCode = ctk.CTkButton(
            master=self.ConfirmAccessCode, 
            image=hideEyeImage, 
            text="", 
            width=3, 
            height=3, 
            fg_color='#FFFFFF', 
            text_color='#393839', 
            hover_color='#FFFFFF',
            command=lambda: togglePassword(self.ConfirmAccessCode, viewConfirmedAccessCode, self.confirm_code_hidden)
        ) 
        viewConfirmedAccessCode.grid(row=0, column=0, sticky='e', padx=(0,10))
        
        
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
        self.dataInput = ctk.CTkEntry(
            master=dataInputFrame, 
            placeholder_text='Enter Message...', 
            placeholder_text_color='#393839', 
            font=('Sniglet', 20), 
            fg_color="white", 
            width=230, 
            height=130
        )
        self.dataInput.grid(row=0, column=0, padx=5, pady=5)
        
        #or
        orLabel = ctk.CTkLabel(master=embedPageContent, text='or', font=('Sniglet', 24), text_color="#a63a50")
        orLabel.grid(row=4, column=3, padx=(0,50))
        
        #Text file upload button
        fileUploadButton = ctk.CTkButton(master=embedPageContent,
                                    text='Upload File',
                                    text_color='white',
                                    border_color='#393839',
                                    corner_radius = 100,
                                    fg_color= '#393839',
                                    font=('Lalezar', 22),
                                    command=openTextFile, 
                                    height=40)
        fileUploadButton.grid(row=5, column=3, pady=(0,0), padx=(0,50))  

        #Chosen text file display placeholder

        fileUploadLabelFrame = ctk.CTkLabel(
                    embedPageContent,
                    fg_color="#393839",
                    corner_radius=100,
                    width=230,
                    height=25
                )
        fileUploadLabelFrame.grid(row=6, column=3, padx=(0,40), pady=(10, 0))

        fileUploadLabel = ctk.CTkLabel(master=fileUploadLabelFrame,
                                    textvariable=self.selectedTextFile,
                                    corner_radius = 100,
                                    height=25,
                                    width=230,
                                    fg_color= '#FFFFFF',
                                    text_color="#393839")
        fileUploadLabel.grid(row=0, column=0, padx=10, pady=6)

        noteEncryption = ctk.CTkLabel(
            embedPageContent,
            font=("Lalezar", 17),
            text_color='#a63a50',
            text = "Data will be encrpyted automatically."
        )
        noteEncryption.grid(row=8, column=3,padx=(0,40))


        #Delete button for chosen Text file display
        deleteButton = ctk.CTkButton(master=fileUploadLabel, text='x', height=0.5, width=1, hover_color="#FFFFFF", text_color="#a63a50", fg_color="#FFFFFF", command= deleteText, font=("Sniglet", 22)) 
        deleteButton.grid(row=0, column=0, sticky='e', padx=(0,20), pady=(0,3))

        #Submit button--------------------
        submitButton = ctk.CTkButton(master=embedPageContent,
                                    text='Embed Audio',
                                    text_color='#FFFFFF',
                                    corner_radius = 100,
                                    fg_color= '#a63a50',
                                    font=('Lalezar', 22),
                                    height=50,
                                    command = submitAction)
        submitButton.grid(row=9, padx=(302,0), pady=(30,0))

        self.statusLabel = ctk.CTkLabel(
            master=embedPageContent,
            text="", 
            text_color='#393839',
            font=('Lalezar', 16)
        )
        self.statusLabel.grid(row=10, column=2, pady=(10,0)) 

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

        #This function hides and shows entered access code
        def togglePassword(entry, button, hidden):
            if hidden[0]:  # If currently hidden
                entry.configure(show="")  # Show text
                button.configure(image=openEyeImage)  # Set open eye icon
            else:
                entry.configure(show="*")  # Hide text
                button.configure(image=hideEyeImage)  # Set hide eye icon
            hidden[0] = not hidden[0]  # Toggle the state
        
        # Initialize the toggle state
        self.input_code_hidden = [True]
        self.confirm_code_hidden = [True]

        # Load and prepare the images
        hideEyeImage = ctk.CTkImage(
            light_image=Image.open("Images\\HideEye.png"),
            size=(10, 10) 
        )

        openEyeImage = ctk.CTkImage(
            light_image=Image.open("Images\\OpenEye.png"), 
            size=(10, 10)  
        )
 
        #Variable holding selected audio file
        self.selectedAudioFile = ctk.StringVar(value="No File Selected")
 
        #Function to browse and open audio file
        def openAudioFile():
          filePath = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
          if filePath:
           #Chosen audio display
            fileName = os.path.basename(filePath)
            self.selectedAudioFile.set(fileName)  
            self.fullAudioPath = filePath 
            print(f"Selected file: {filePath}")
 
        #Function to delete selected audio file
        def deleteAudio():
            self.selectedAudioFile.set("No File Selected")
            if hasattr(self, 'fullAudioPath'):
                delattr(self, 'fullAudioPath')

        def decoder():
            try:
                # Getting the access code
                accessCode = self.accessCodeInput.get()
                
                #Audio to be extracted is chosen and loaded
                audioPath = getattr(self, 'fullAudioPath', None)
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
                
                # Sending the decrypted data to success page
                success_page = self.controller.frames[ExtractSuccessPage]
                success_page.setData(decrypted_data, self.selectedAudioFile.get())
                self.controller.show_frame(ExtractSuccessPage)
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to extract and decrypt data: {str(e)}")
 
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
            text='Upload Audio',
            text_color='#ffffff',
            border_color='#393839',
            corner_radius = 100,
            fg_color= '#393839',
            font=('Lalezar', 24),
            command=openAudioFile,
            height=40) 
        audioUploadButton.grid(row=3, column=1, padx=(0,260), pady=(100,20))
 
        audioFileLabelFrame = ctk.CTkFrame(
            extractPageContent,
            fg_color="#393839",
            corner_radius=100,
        )
        audioFileLabelFrame.grid(row=4, column=1, padx=(0,260), pady=(10,0))

        #Chosen audio display
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

        # Access Code input
        accessCodeLabel = ctk.CTkLabel(master=extractPageContent, 
                                    text='Enter Access Code', 
                                    text_color='#393839', 
                                    font=('Sniglet', 20))
        accessCodeLabel.grid(row=5, column=1, padx=(0,260), pady=(20,0))

        accessCodeFrame = ctk.CTkFrame(
            extractPageContent,
            fg_color="#393839",
            corner_radius=100,
        )
        accessCodeFrame.grid(row=6, column=1, padx=(0,260))

        self.accessCodeInput = ctk.CTkEntry(
            master=accessCodeFrame, 
            fg_color="white",
            corner_radius=100,
            width=180,
            height=28,
            show="*",
            placeholder_text="..."
        )
        self.accessCodeInput.grid(row=0, column=0, padx=5, pady=5)

        # Button for toggling password visibility
        toggleButton = ctk.CTkButton(
            master=accessCodeFrame,
            image=hideEyeImage, text ="", width=3, height=3, fg_color='#FFFFFF', text_color='#393839', hover_color='#FFFFFF',
            command=lambda: togglePassword(self.accessCodeInput, toggleButton, self.input_code_hidden)
        )
        toggleButton.grid(row=0, column=0, sticky='e', padx=(0,10))
 
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

class ExtractSuccessPage(BasePage):
    def __init__(self, parent, controller):
        self.fileName = ""
        self.extractedData = ""
        super().__init__(parent, controller)
        
    def setData(self, data, fileName):
        self.extractedData = data
        self.fileName = fileName
        self.updateDisplay()
        
    def updateDisplay(self):
        if hasattr(self, 'dataDisplay'):
            self.dataDisplay.delete(1.0, tk.END)
            self.dataDisplay.insert(tk.END, self.extractedData)
        if hasattr(self, 'fileName_label'):
            self.fileName_label.configure(text=self.fileName)
            
    def create_content(self):
        success_frame = ctk.CTkFrame(self.contentFrame, fg_color='White', corner_radius=10)
        success_frame.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        success_frame.grid_columnconfigure((0, 1), weight=1)
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        backArrowPath = os.path.join(current_dir, "Images", "BackArrow.png")
        
        self.backArrow = ctk.CTkImage(light_image=Image.open(backArrowPath), size=(40,40))
        self.backArrowButton = ctk.CTkButton(
            success_frame,
            image=self.backArrow,
            text="",
            fg_color="transparent",
            command=lambda: self.controller.show_frame(HomePage))
        self.backArrowButton.grid(row=0, column=0, padx=(0,0), ipadx=0, ipady=0)
        
        # File name display
        self.fileLabel = ctk.CTkLabel(
            success_frame,
            text="File Uploaded:",
            font=('Sniglet', 20),
            text_color='#393839'
        )
        self.fileLabel.grid(row=1, column=1, padx=(0,260), pady=(20,10))
        
        # File name frame
        fileFrame = ctk.CTkFrame(
            success_frame,
            fg_color="#393839",
            corner_radius=100,
        )
        fileFrame.grid(row=2, column=1, padx=(0,260))
        
        self.fileName_label = ctk.CTkLabel(
            fileFrame,
            text=self.fileName,  # fileName is initialized here
            font=('Lalezar', 16),
            fg_color='white',
            corner_radius=100,
            width=260,
            height=35
        )
        self.fileName_label.grid(row=0, column=0, padx=10, pady=6)
        
        # Data label
        dataLabel = ctk.CTkLabel(
            success_frame,
            text="Data:",
            font=('Sniglet', 20),
            text_color='#393839'
        )
        dataLabel.grid(row=3, column=1, padx=(0,260), pady=(20,10))

        dataFrame = ctk.CTkFrame(
            success_frame,
            fg_color="#393839",
            corner_radius=10,
        )
        dataFrame.grid(row=4, column=1, padx=(0,260), pady=(0,20))
        
        # Data display
        self.dataDisplay = ctk.CTkTextbox(
            dataFrame,
            width=230, 
            height=130,
            corner_radius=10
        )
        self.dataDisplay.grid(row=0, column=0, padx=10, pady=6)
        if self.extractedData:  # adding the data if it exists
            self.dataDisplay.insert(tk.END, self.extractedData)

        # Return home button
        returnHomeButton = ctk.CTkButton(
            success_frame,
            text='Return Home',
            text_color='#FFFFFF',
            corner_radius=10,
            fg_color='#a63a50',
            font=('Lalezar', 30),
            command=lambda: self.controller.show_frame(HomePage)
        )
        returnHomeButton.grid(row=5, column=1, padx=(0,260), pady=(20,0))

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
        self.db_manager = DatabaseManager()

        # Main container for all content
        helpContactPageContent = ctk.CTkFrame(self.contentFrame, fg_color="white")
        helpContactPageContent.grid(row=1, column=1, sticky="nsew")
        helpContactPageContent.grid_columnconfigure(0, weight=1)
        helpContactPageContent.grid_rowconfigure(1, weight=1)

        # Back Arrow
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
        self.backArrowButton.grid(row=0, column=0, padx=(20,0), pady=(20,0), sticky='w')

        # Main content container
        mainContent = ctk.CTkFrame(helpContactPageContent, fg_color="#FEFCFB")
        mainContent.grid(row=1, column=0, sticky="n")
        mainContent.grid_columnconfigure((0,1), weight=1)

        # Page title
        headLabel = ctk.CTkLabel(
            master=mainContent, 
            text='Need Help?', 
            font=('Sniglet', 50),
            text_color='#a63a50'
        )
        headLabel.grid(row=0, column=0, columnspan=2, pady=(0,30))

       
        infoFrame = ctk.CTkFrame(mainContent, fg_color="#393839", corner_radius=25)
        infoFrame.grid(row=1, column=0, padx=(40,20), pady=(0,50))
        
        infoText = ctk.CTkLabel(master=infoFrame, font=('Inter', 20), fg_color="white", width=280, height=180, corner_radius=10, text="Information on how\nsteganography works can\nbe found on the home\npage or the about page.\nTo contact us, use the\nform here.")
        infoText.grid(row=2, column=3, padx=12, pady=12, rowspan=2)


        # Form container
        formContainer = ctk.CTkFrame(mainContent, fg_color="#FEFCFB")
        formContainer.grid(row=1, column=1, padx=(20,40), sticky="n")

        enterEmailLabel = ctk.CTkLabel(
            formContainer,
            text="Enter Email:",
            font=('Sniglet', 20)
            )
        enterEmailLabel.grid(row=0, column=0, sticky='w', padx=(20,0))

        emailEntryFrame = ctk.CTkFrame(
            formContainer,
            fg_color="#393839",
            corner_radius=100
        )
        emailEntryFrame.grid(row=1, column=0, pady=(0,20))
        
        # Email input
        self.emailEntry = ctk.CTkEntry(
            emailEntryFrame,
            width=300,
            height=40,
            corner_radius=20,
            border_width=2,
            border_color="#E5E5E5",
            fg_color="white",
            text_color="black"
        )
        self.emailEntry.grid(row=0, column=0, padx=10, pady=6)

        contactMessageFrame = ctk.CTkFrame(
            formContainer,
            fg_color="#393839",
            corner_radius=10
        )
        contactMessageFrame.grid(row=2, column=0, pady=(0,20))

        # Message input
        self.contactMessage = ctk.CTkTextbox(
            contactMessageFrame,
            width=300,
            height=100,
            corner_radius=20,
            fg_color="white",
            text_color="black",
            font=('Sniglet', 20)
        )
        self.contactMessage.insert("1.0", "Enter Message...")
        self.contactMessage.grid(row=0, column=0, padx=8, pady=8, sticky='n')

        # Submit button
        submitButton = ctk.CTkButton(
            helpContactPageContent,
            text="Send",
            font=('Lalezar', 20),
            text_color="white",
            fg_color="#a63a50",
            hover_color="#8b3143",
            corner_radius=20,
            width=150,
            height=55,
            command=self.submit_form
        )
        submitButton.grid(row=2, column=0, pady=(0,100))

        # Status label for feedback
        self.statusLabel = ctk.CTkLabel(
            formContainer,
            text="",
            font=('Segoe UI', 14),
            text_color='black'
        )
        self.statusLabel.grid(row=4, column=0, pady=(0,20))

    def validate_email(self, email):
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def submit_form(self):
        email = self.emailEntry.get().strip()
        message = self.contactMessage.get("1.0", "end-1c").strip()

        # Validation
        if not all([email, message]):
            self.statusLabel.configure(text="Please fill in all fields", text_color="#FFB6C1")
            return

        if not self.validate_email(email):
            self.statusLabel.configure(text="Please enter a valid email address", text_color="#FFB6C1")
            return

        try:
            # Save to database
            self.db_manager.save_contact(email, message)
            
            # Clear form
            self.emailEntry.delete(0, 'end')
            self.contactMessage.delete("1.0", "end")
            self.contactMessage.insert("1.0", "Enter Message...")
            
            # Show success message
            self.statusLabel.configure(text="Message sent successfully!", text_color="#90EE90")
        except Exception as e:
            self.statusLabel.configure(text="Error sending message. Please try again.", text_color="#FFB6C1")
            print(f"Database error: {e}")




