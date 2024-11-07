import customtkinter as ctk
import customtkinter
from PIL import Image
import os
from tkinter import filedialog

class Sidebar(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#393839")
        self.controller=controller
        self.menuExpanded=False
        self.collapsedWidth=100
        self.expandedWidth=265

        self.menuExpanded = controller.sidebarExpanded

        self.configure(width=self.collapsedWidth)
        self.grid_rowconfigure(1, weight=1)
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
            command=self.toggleMenu)
        self.menuIconButton.grid(row=1, column=0, sticky="new", padx=(0,0), ipadx=0, ipady=0)
        

        # Menu Frame (initially hidden)
        self.menuFrame = ctk.CTkFrame(self, fg_color="#2d2d2d", corner_radius=8)

    def toggleMenu(self):
        if not self.menuExpanded:
            self.configure(width = self.expandedWidth)
            self.menuFrame.grid(row=1, column=0, padx=5, pady=(5, 5), sticky="new")
            # About button
            aboutButton = ctk.CTkButton(            
                self.menuFrame, 
                text="About", 
                command=lambda: self.controller.show_frame(AboutPage),
                text_color='White',
                fg_color='transparent',
                corner_radius=10,
                anchor="w")
            aboutButton.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

            helpContactButton = ctk.CTkButton(            
                self.menuFrame, 
                text="Help / Contact Us", 
                command=lambda: self.controller.show_frame(HelpContactPage),
                text_color='White',
                fg_color='transparent',
                corner_radius=10,
                anchor="w")
            helpContactButton.grid(row=2, column=1, padx=20, pady=20, sticky="ew")

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
        
  
    
    def create_content(self):
        # Must be implemented by all child classes 
        raise NotImplementedError

class HomePage(BasePage):

    def create_content(self):

        # *************** !!!!!!!!!!!!!!!!!!! ----------------

        

        # Home page content
        homePageContent = ctk.CTkFrame(self.contentFrame, fg_color='White', corner_radius=10)
        homePageContent.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        homePageContent.grid_columnconfigure((0, 1), weight=1)


        # CloakCast label
        label = ctk.CTkLabel(homePageContent, text="CloakCast", font=("Lalezar", 130), text_color="#a63a50", fg_color="white")
        label.grid(row=0, column=0, padx=10, pady=20, sticky="ew", columnspan=2)

        # Embed button
        embedButton = ctk.CTkButton(
            homePageContent, 
            text="Embed", 
            command=lambda: self.controller.show_frame(EmbedPage),
            text_color='White',
            fg_color='#393839',
            corner_radius=10,
            font=('Lalezar', 60))
        embedButton.grid(row=1, column=0, padx=20, pady=15, ipadx=20, ipady=5)

        # Extract button
        extractButton = ctk.CTkButton(            
            homePageContent, 
            text="Extract", 
            command=lambda: self.controller.show_frame(ExtractPage),
            text_color='White',
            fg_color='#393839',
            corner_radius=10,
            font=('Lalezar', 60))
        extractButton.grid(row=1, column=1, padx=20, pady=15, ipadx=20, ipady=5)

class EmbedPage(BasePage):

    def create_content(self):

        #Functions--------------------

        #Variable holding selected audio file
        selectedAudioFile = ctk.StringVar()
        selectedAudioFile = set("No File Selected")
 
        #Function to browse and open audio file
        def openAudioFile():
          filePath = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
          if filePath:
           print(f"Selected file: {filePath}")
 
        #Function to delete selected audio file
        def deleteAudio():
            selectedAudioFile = set("No File Selected")
            deleteButton.configure(state=ctk.NORMAL) #Active only when a file has been selected

        #Content--------------------

        embedPageContent = ctk.CTkFrame(master = self, fg_color='White') # this is the content window
        embedPageContent.grid(padx=500, pady=250)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        backArrowPath = os.path.join(current_dir, "Images", "BackArrow.png")

        self.backArrow = ctk.CTkImage(light_image=Image.open(backArrowPath), size=(40,40))
        self.backArrowButton = ctk.CTkButton(
            embedPageContent, 
            image=self.backArrow, 
            text="", 
            fg_color="transparent",
            command=lambda: self.controller.show_frame(HomePage))
        self.backArrowButton.grid(row=0, column=0, padx=(0,0), ipadx=0, ipady=0)

        #Cover Media--------------------
 
        coverMediaLabel = ctk.CTkLabel(master=embedPageContent, text='Cover Media', text_color='#a63a50', font=('lalezar', 40))
        coverMediaLabel.grid(row=1, column=0)
        
        #Audio upload button
        audioUploadButton = ctk.CTkButton(master=embedPageContent,
                                    text='Upload Audio',
                                    text_color='#a63a50',
                                    border_width= 3,
                                    border_color='#393839',
                                    corner_radius = 10,
                                    fg_color= '#FFFFFF',
                                    font=('Lalezar', 30),
                                    command=openAudioFile) #Needs to be added
        audioUploadButton.grid(row=2, column=0, pady=20)
        
        
        #Chosen audio display
        audioFileLabel = ctk.CTkLabel(master=embedPageContent,
                                    textvariable= selectedAudioFile,
                                    fg_color= 'blue',
                                    corner_radius = 10)
        audioFileLabel.grid(row=3, column=0)
        
        #Delete button for chosen audio file display
        deleteButton = ctk.CTkButton(master=embedPageContent, text='x', width=3, command= deleteAudio) #Trash icon button placeholder
        deleteButton.grid(row=2, column=2)
        
        
        #Access Code--------------------
        
        #Header
        accessCodeLabel = ctk.CTkLabel(master=embedPageContent, text='Access Code', text_color='#a63a50', font=('lalezar', 40))
        accessCodeLabel.grid(row=3, column=0)
        
        enterCodeLabel = ctk.CTkLabel(master=embedPageContent, text='Enter Code', text_color='#393839', font=('lalezar', 20))
        enterCodeLabel.grid(row=4, column=0)
        
        #Input field
        inputAccessCode = ctk.CTkEntry(master=embedPageContent)
        #took away string variable for placeholder text to work
        inputAccessCode = ctk.CTkEntry(master=embedPageContent, placeholder_text='...', placeholder_text_color='#393839')
        inputAccessCode.grid(row=5, column=0)
        
        #View access code button
        viewAccessCode = ctk.CTkButton(master=embedPageContent, text='o', width=3) #eye icon button placeholder
        viewAccessCode.grid(row=5, column=1)
        
        confirmCodeLabel = ctk.CTkLabel(master=embedPageContent, text='Confirm Code', width=50, text_color='#393839', font=('lalezar', 20))
        confirmCodeLabel.grid(row=6, column=0)
        
        #Confirm input field
        #Input field
        ConfirmAccessCode = ctk.CTkEntry(master=embedPageContent)
        #took away string variable for placeholder text to work
        ConfirmAccessCode = ctk.CTkEntry(master=embedPageContent, placeholder_text='...', placeholder_text_color='#393839')
        ConfirmAccessCode.grid(row=7, column=0)
        
        #View confirmed access code button
        viewConfirmedAccessCode = ctk.CTkButton(master=embedPageContent, text='-', width=3) #eye icon button placeholder
        viewConfirmedAccessCode.grid(row=7, column=1)
        
        
        #Hidden Data--------------------
        
        hiddenDataLabel = ctk.CTkLabel(master=embedPageContent, text='Hidden Data', text_color='#a63a50', font=('Lalezar', 40))
        hiddenDataLabel.grid(row=0, column=3)
        
        #Input field
        input = ctk.CTkEntry(master=embedPageContent)
        #took away string variable for placeholder text to work
        input = ctk.CTkEntry(master=embedPageContent, placeholder_text='Enter Message...', placeholder_text_color='#393839')
        input.grid(row=1, column=3)
        
        #or
        orLabel = ctk.CTkLabel(master=embedPageContent, text='Or', font=('Lalezar', 20))
        orLabel.grid(row=2, column=3)
        
        #Text file upload button
        audioUploadButton = ctk.CTkButton(master=embedPageContent,
                                    text='Upload File',
                                    text_color='#a63a50',
                                    border_width= 3,
                                    border_color='#393839',
                                    corner_radius = 10,
                                    fg_color= '#FFFFFF',
                                    font=('Lalezar', 30)) #Needs to be added
        audioUploadButton.grid(row=3, column=3, pady=20)
        
        #Chosen text file display placeholder
        fileUploadLabel = ctk.CTkLabel(master=embedPageContent,
                                    text='fiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiile',
                                    fg_color= 'red',
                                    corner_radius = 10) #File display placeholder
        fileUploadLabel.grid(row=4, column=3)
        
        #Delete button for chosen Text file display
        deleteButton = ctk.CTkButton(master=embedPageContent, text='x', width=3) #Trash icon button placeholder
        deleteButton.grid(row=4, column=4)
        
class ExtractPage(BasePage):

    def create_content(self):

        #Functions--------------------

        #Variable holding selected audio file
        selectedAudioFile = ctk.StringVar()
        selectedAudioFile = set("No File Selected")
 
        #Function to browse and open audio file
        def openAudioFile():
          filePath = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
          if filePath:
           print(f"Selected file: {filePath}")
 
        #Function to delete selected audio file
        def deleteAudio():
            selectedAudioFile = set("No File Selected")
            deleteButton.configure(state=ctk.NORMAL) #Active only when a file has been selected


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
        audioUploadButton.grid(row=0, column=1, sticky="w", pady=120, ipadx=10, ipady=10)



        #Chosen audio display 
        audioFileLabel = ctk.CTkLabel(master=extractPageContent,
                                    textvariable= selectedAudioFile,
                                    fg_color= 'blue',
                                    corner_radius = 10)
        audioFileLabel.grid(row=1, column=1, sticky="w", padx=50, columnspan=1)
        
        #Delete button for chosen audio file display
       # deleteButton = ctk.CTkButton(master=extractPageContent, text='x', width=3, command= deleteAudio) #Trash icon button placeholder
       # deleteButton.grid(row=3, column=2)

class AboutPage(BasePage):

    def create_content(self):

        aboutPageContent = ctk.CTkFrame(self.contentFrame, fg_color='White', corner_radius=10)
        aboutPageContent.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        aboutPageContent.grid_columnconfigure((0, 1), weight=1)

        # Back arrow that returns user to home
        current_dir = os.path.dirname(os.path.abspath(__file__))
        backArrowPath = os.path.join(current_dir, "Images", "BackArrow.png")

        self.backArrow = ctk.CTkImage(light_image=Image.open(backArrowPath), size=(40,40))
        self.backArrowButton = ctk.CTkButton(
            aboutPageContent, 
            image=self.backArrow, 
            text="", 
            fg_color="transparent",
            command=lambda: (
                self.sidebar.collapse_menu(),
                self.controller.show_frame(HomePage)
            )
        )
        
        self.backArrowButton.grid(row=0, column=0, padx=(0,0), ipadx=0, ipady=0)
        
        headLabel = ctk.CTkLabel(master=aboutPageContent, text='ABOUT', font=('Lalezar', 50))
        headLabel.grid(row=1, column=1, sticky="w")

         # Embed button
        aButton = ctk.CTkButton(
            aboutPageContent, 
            text="Im a button xx", 
            command=lambda: self.controller.show_frame(EmbedPage),
            text_color='White',
            fg_color='#393839',
            corner_radius=10,
            font=('Lalezar', 30))
        aButton.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

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