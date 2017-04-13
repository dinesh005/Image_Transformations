import cv2
import numpy as np
import math
import imutils
image=cv2.imread('emma.jpg')
print image.shape
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray=imutils.resize(gray,width=400)
print image[0][0][0]
(m,n,p)=image.shape
x=input()
y=input()
resized=np.zeros([x*m , y*n , p],dtype="uint8")
count=0
for i in range(x*m):
    for j in range(y*n):
        x1=math.floor(j//x)
        y1=math.floor(i//y)
        for k in range(p):
            print count
            resized[i][j][k]=image[y1][x1][k]
            count+=1
cv2.imshow('Original Image',image)
cv2.imshow('Resized Image',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
