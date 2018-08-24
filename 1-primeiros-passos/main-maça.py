import cv2
import numpy

img= cv2.imread("maca.ppm")

altura=img.shape[0]
largura=img.shape[1]
canais=img.shape[2]

for i in range(altura):
	for j in range(largura):
		if (img[i,j,2] > 110 and img[i,j,1]<140 and img[i,j,0]<140):
			img[i,j,2]= 15
			img[i,j,0]=255

cv2.imwrite("maca1.ppm", img)
print("Imagem gerada com sucesso!")