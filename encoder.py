from stepic import encode
from eyed3 import load
from PIL import Image

print("##########################")

#Gaining secret data
data = str(input("YOUR DATA: "))

#Audio file is chosen
audio = input("AUDIO: ")
#Image to cover audio is chosen
imgName = input("IMAGE: ")
audio = load(audio) #Opens the audio

#Opens the image and puts the secret text inside saves it
img = Image.open(imgName)
imgStegano = encode(img, data.encode())
imgStegano.save(imgName)

#Making the image the cover of the audio
audio.initTag()
audio.tag.images.set(3, open(imgName, "rb").read(), "image/png")
audio.tag.save()

print("##########################")

#Instructions to exit the program
input("COMPLETE(presss enter -> exit) ")