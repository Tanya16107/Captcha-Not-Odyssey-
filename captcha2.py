import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('download.png')
#-------blurs the image-------------------

blur = cv2.blur(img,(5,5))
# plt.imshow(blur)
# plt.show()

#--------------median blur-------------


median = cv2.medianBlur(img,5)
# plt.imshow(median)
# plt.show()


#------perspective transformation------
rows,cols,ch = blur.shape

pts1 = np.float32([[0,0],[350,50],[10,80],[256,300]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(blur,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
