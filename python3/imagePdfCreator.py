from PIL import Image
import os
import glob

fileList = glob.glob("/Users/alexpreston/Desktop/*.jpeg") #Absolute Paths for Mac Users

print(fileList)

imagelist = []

for image in fileList:
    image = Image.open(image)
    im1 = image.convert('RGB')
    imagelist.append(im1)

im1.save(r'/Users/alexpreston/Desktop/myImages.pdf',save_all=True, append_images=imagelist)