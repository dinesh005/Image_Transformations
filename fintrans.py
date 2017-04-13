import cv2
import numpy as np
import imutils
image=cv2.imread('emma.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
x=input()
y=input()
#gray=imutils.resize(gray,width=400)

m=image.shape[0]
n=image.shape[1]
p=image.shape[2]
print m,n
trans=np.zeros([(x+m),(y+n),p],dtype='uint8')
for i in range(m):
    for j in range(n):
            x1=x+i
            y1=y+j
            for k in range(p):
                trans[x1][y1][k]=image[i][j][k]
cv2.imshow('Original Image',image)
cv2.imshow('Translated Image',trans)
cv2.waitKey(0)
cv2.destroyAllWindows()
