from stepic import decode
from eyed3 import load
from PIL import Image
from os import system

print("##########################")

#Audio to be extracted is chosen and loaded
audio = input("Audio: ")
audio = load(audio)

#Creating an image to save the secret text to, from the cover of the song
img = open("tempImg.png","wb")
img.write(audio.tag.images[0].image_data)
img.close()

#The secret text is save in the temp image
img = Image.open("tempImg.png")
text = decode(img)
system("del tempImg.png") #Deleting the temp image
print("Data is: "+ str(text)) #Displaying the text

print("##########################")

#Instructions to exit the program
input(" complete(press enter -> exit) ")