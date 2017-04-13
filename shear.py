import cv2
import numpy as np
import imutils
import math
image=cv2.imread('emma.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
rads=input()
gray=imutils.resize(gray,width=400)
sheared_deg=1//(math.tan((2*math.pi*rads)/360))
m=image.shape[0]
n=image.shape[1]
p=image.shape[2]
print m,n
shear=np.zeros([m,((sheared_deg*n )+ m),p],dtype='uint8')
for i in range(m):
    for j in range(n):
            y1=math.ceil((sheared_deg*j )+i)
            x1=i
            for k in range(p):
                shear[x1][y1][k]=image[i][j][k]
cv2.imshow('Original Image',image)
cv2.imshow('Translated Image',shear)
cv2.waitKey(0)
cv2.destroyAllWindows()
