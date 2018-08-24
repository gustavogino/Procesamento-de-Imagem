import cv2
import numpy

img= cv2.imread("image.pgm",0)
print (img.shape)

#INVERTER IMAGEM
for i in range(240):
	for j in range(210):
		img[i,j]=255-img[i,j] 

cv2.imwrite("image2.pgm", img)


# DAR BRILHO A IMAGEM
img= cv2.imread("image.pgm",0)

for i in range(240):
	for j in range(210):
		if (img[i,j] < 230):
			img[i,j]=img[i,j] + 25

cv2.imwrite("image3.pgm",img)