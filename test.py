from stepic import encode
from eyed3 import load
from PIL import Image

filePath = str(input(" Your file path: "))

with open(filePath, "r") as file:
    data = file.read()

audio = input("Audio: ")
imgName = input(" image: ")
audio = load(audio)

img = Image.open(imgName)
imgStegano = encode(img, data.encode())
imgStegano.save(imgName)

audio.initTag()
audio.tag.images.set(3, open(imgName, "rb").read(), "image/png")
audio.tag.save()