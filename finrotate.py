import cv2
import numpy as np
import math
img=cv2.imread('emma.jpg')
img=cv2.resize(img,(256,256))
rows=img.shape[0]
columns=img.shape[1]
dgf=img.shape[2]
print rows,columns
img1=cv2.getRotationMatrix2D((columns/2,rows/2),30,1)
dst=cv2.warpAffine(img,img1,(columns,rows))


midx=math.ceil((rows+1)/2)
midy=math.ceil((columns+1)/2)
print int(midx)
print int(midy)
rads=input()
#print img[144][144][0]
sdf=int(round(((rows-midx)*math.cos(((math.pi)*rads)/180)) +(-1)*((columns-midy)*math.sin(((math.pi)*rads)/180))))
sdf1=int(round(((rows-midx)*math.sin(((math.pi)*rads)/180)) +((columns-midy)*math.cos(((math.pi)*rads)/180))))
imagerot=np.zeros((sdf,sdf1,dgf),np.uint8)


for i in range(sdf):
        for j in range(sdf1):
            x=round(((i-midx)*math.cos(((math.pi)*rads)/180)) +(-1)*((j-midy)*math.sin(((math.pi)*rads)/180)))
            y=round(((i-midx)*math.sin(((math.pi)*rads)/180)) +((j-midy)*math.cos(((math.pi)*rads)/180)))
            x=int(x+midx)
            y=int(y+midy)
            if x>=1 and y>=1 and x<columns and y<rows:
               # print x,y
                for k in range(dgf):
                    imagerot[i][j][k]=img[x][y][k]

cv2.imshow('Default Rotate',dst)
cv2.imshow('Rotated image',imagerot)

cv2.waitKey(0)
cv2.destroyAllWindows()
