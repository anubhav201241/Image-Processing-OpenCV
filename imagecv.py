import cv2
import numpy as np   
img = cv2.imread('elon.jpg')  #Download picture and paste the format of that image(jpeg,png or jpg) 
img = cv2.resize(img, None , fx=0.5, fy=0.5)  
red_channel = img[:, :, 0]
blue_channel = img[:, :, 1]
green_channel = img[:, :, 2]
#Create Empty image through Numpy Array - every Pixel Value

red_img = np.zeros(img.shape)
blue_img = np.zeros(img.shape)
green_img = np.zeros(img.shape)
                                          #open Cv reads an image as B, G, R  
                                          #Create  empty iimage thorugh empty array evry pixel in this line of code is 0
                                          #Assigning values from red channel to red image

red_img[:, :, 0] = red_channel
blue_img[:, :, 1] = blue_channel
green_img[:, :, 2] = green_channel

#isolated red calue of the image 
cv2.imshow('Red Channel',red_img)
cv2.imshow('Blue channel',blue_img)
cv2.imshow('Green Channel', green_img)
cv2.waitKey()
