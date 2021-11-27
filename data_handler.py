import cv2
import os
import numpy as np
img = cv2.imread("images\SwedenLab.jpg", cv2.IMREAD_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
img_final = cv2.resize(im_bw, (150,200))
np.save('data\sweden.npy', img_final)
cv2.imshow("img", img_final)
cv2.waitKey(0) 
cv2.destroyAllWindows() 