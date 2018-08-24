import cv2
import numpy as np 

img = cv2.imread("estrela.jpg")
#print ("dados da imagem: ",img.shape)
altura=img.shape[0]
largura=img.shape[1]
canais=img.shape[2]

for i in range(altura):
	for j in range(largura):
		if (img[i,j,2] < 160 and img[i,j,1] < 255 and img[i,j,0] < 255):

			img[i,j,2] = 255
			img[i,j,1] = 255
			img[i,j,0] = 255

cv2.imwrite("estrela-cubo.jpg",img)
print("Imagem gerada com sucesso!")			


