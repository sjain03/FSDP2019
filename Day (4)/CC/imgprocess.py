# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:14:28 2019

@author: Sahil
"""


"""
Code Challenge
  Name: 
    Image Processing using PIL
  Filename: 
    imgprocess.py
  Problem Statement:
    Given an image, perform image processing operations. 

    Keep only one output image i.e perform all tasks on the same image (override) 
    and print only the name of your output image with extension name in the end of your program. 

    Take the Image name from User (Handle the extension for image file name in your code)
    
    The image processing features to be provided by your code are:

        a.     Greyscale
        b.     Rotate_90 (Rotate the given image file by 90 clockwise)
        c.     Crop (Center) (size = 160(W), 204(H))
        d.     Thumbnail – Generate the thumbnail of the given image (size = 75, 75)
    
"""

from PIL import Image
x = input("Enter the name of Image >")
img = Image.open(x)
#img.size()
#img.close()

img_greyscale = img.convert('LA')
#img_greyscale.show()
#img_greyscale.save('a_greyscale.jpg')

img_rotate = img_greyscale.transpose(Image.ROTATE_90)
#img_rotate.show()
#img_rotate.save('a_rotate.jpg')



width, height = img_rotate.size
hw = width/2
hh = height/2
box =(hw-80,hh-102,hw+80,hh+102)

img_crop = img_rotate.crop(box)


#img_crop.show()


#img_crop.save('a_crop.jpg')


img_crop.thumbnail((75,75))
img_crop.save('a_thumb.png')

final_img = Image.open("a_thumb.png")
final_img.show()

print(final_img.filename)




