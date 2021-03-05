import random

file = open("source.png", "rb")
image = bytearray(file.read()) 
file.close()

key = random.randint(0, 255)

for i in range(len(image)):
    image[i] = image[i] ^ key

encrypted = open("mystery", "wb")
encrypted.write(image)
encrypted.close()