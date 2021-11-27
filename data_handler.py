import cv2
import os
import numpy as np
img = cv2.imread("images\somaiya.jpeg", cv2.IMREAD_GRAYSCALE)
# img_f = cv2.resize(img, (150,200))
(thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(np.unique(im_bw))


for i, v1 in enumerate(im_bw):
    for j, v2 in enumerate(v1):
        if v2 == 255:
            im_bw[i, j] = 1

np.save('data\somaiya.npy', im_bw)
cv2.imshow("img", im_bw)
cv2.waitKey(0) 
cv2.destroyAllWindows() 