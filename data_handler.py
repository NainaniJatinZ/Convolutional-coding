import cv2
import os
import numpy as np


# TO CREATE .NPY FILES FROM IMAGES


path = "images\somaiya.jpeg"  # Change this to the image of your choice
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 
(thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(np.unique(im_bw))  # This will give an binary image with 0s and 255s

for i, v1 in enumerate(im_bw):      # as we need a binary array with 0s and 1s we will use the following code
    for j, v2 in enumerate(v1):
        if v2 == 255:
            im_bw[i, j] = 1

np.save('data\somaiya.npy', im_bw) #saving in npy format, change the path here as well
cv2.imshow("img", im_bw)
cv2.waitKey(0) 
cv2.destroyAllWindows() 