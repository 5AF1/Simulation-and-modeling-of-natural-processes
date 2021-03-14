# -*- coding: utf-8 -*-
# Copyright (C) 2016 Universite de Geneve, Switzerland
# E-mail contact: sebastien.leclaire@etu.unige.ch
#
# The Parity Rule
#

from numpy import *
import matplotlib.pyplot as plt
from matplotlib import cm
import copy
import imageio



def parity():
    s0,s1,s2,s3,s4 = [False,False,False,False,False]
    while s4 != True:
        index = int(s0)+2*int(s1)+4*int(s2)+8*int(s3)
        s = int(s0)+int(s1)+int(s2)+int(s3)
        #print(f"{index} {s%2}")
        lookup[index] = s%2
        if s0 and s1 and s2 and s3:
            s0, s1, s2, s3 ,s4= [not s0, not s1, not s2, not s3,not s4]
        elif s0 and s1 and s2:
            s0, s1, s2, s3 = [not s0, not s1, not s2, not s3]
        elif s0 and s1:
            s0, s1, s2 = [not s0, not s1, not s2]
        elif s0:
            s0, s1 = [not s0, not s1]
        else:
            s0 = not s0


# Definition of functions
def readImage(string): # This function only work for monochrome BMP.
    image =  imageio.imread(string)
    image[image == 255] = 1
    image = image.astype(int)
    return image # Note that the image output is a numPy array of type "int".

# Main Program

# Program input, i.e. the name of the image "imageName" and the maximum number of iteration "maxIter"
imageName = 'image3.bmp'
maxIter   = 32
lookup = {}
# Read the image and store it in the array "image"
parity()
image = readImage(imageName) # Note that "image" is a numPy array of type "int".
# Its element are obtained as image[i,j]
# Also, in the array "image" a white pixel correspond to an entry of 1 and a black pixel to an entry of 0.

# Get the shape of the image , i.e. the number of pixels horizontally and vertically.
# Note that the function shape return a type "tuple" (vertical_size,horizontal_size)
imageSize = shape(image);

# Print to screen the initial image.
print('Initial image:')
plt.clf()
plt.imshow(image, cmap=cm.gray)
plt.show()
plt.pause(0.1)

# Main loop
for it in range(1,maxIter+1):

    imageCopy = copy.copy(image);

    # You need to write here the core of the parity rule algorithm.
    # Altough not mandatory, you might need to use the array "imageCopy" and the tuple "imageSize".
    #
    # Code that you need to write...
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            s0 = image[i-1][j]
            s1 = image[(i+1)%image.shape[0]][j]
            s2 = image[i][j-1]
            s3 = image[i][(j+1)%image.shape[1]]
            imageCopy[i][j] = lookup[int(s0)+2*int(s1)+4*int(s2)+8*int(s3)]

    image = copy.copy(imageCopy)
    # Code that you need to write...

    # Print to screen the image after each iteration.
    if it%16 == 0:
        print('Image after', it, 'iterations:')
        plt.clf()
        plt.imshow(image, cmap=cm.gray)
        plt.show()
        plt.pause(0.1)

# Print to screen the number of white pixels in the final image
print("The number of white pixels after",it,"iterations is: ", sum(image))
