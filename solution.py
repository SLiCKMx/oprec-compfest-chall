file = open("mystery", "rb")
image = file.read() 
file.close() 

image = bytearray(image)
image_try = image.copy()

for i in range(0, 256):
    for j in range(len(image)):
        image_try[j] = image[j] ^ i
    if(image_try[:8] == bytearray([int(k, 16) for k in "89 50 4E 47 0D 0A 1A 0A".split()])):
        solved_file = open("solved.png", "wb")
        solved_file.write(image_try)
        solved_file.close()
        exit()