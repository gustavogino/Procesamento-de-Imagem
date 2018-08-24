import cv2
import numpy as np

#IMAGEM INVERTIDA
img = cv2.imread("colorida.ppm")
print ("Tamanho da imagem: ",img.shape)

for i in range(240):
	for j in range(210):
		img[i,j,0]=255-img[i,j,0]
		img[i,j,1]=255-img[i,j,1]
		img[i,j,2]=255-img[i,j,2]

cv2.imwrite("colorida2.ppm",img)
print("Imagem invertida salva!")

#IMAGEM BRILHO
img = cv2.imread("colorida.ppm")

for i in range(240):
	for j in range(210):
		if (img[i,j,0]< 230):
			img[i,j,0]=img[i,j,0] + 25

		if (img[i,j,1]< 230):
			img[i,j,1]=img[i,j,1] + 25

		if (img[i,j,2]< 230):
			img[i,j,2]=img[i,j,2] + 25


cv2.imwrite("colorida3.ppm",img)
print("Imagem com brilho salva!")