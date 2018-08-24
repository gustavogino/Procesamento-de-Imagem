import cv2
import numpy as np

img = cv2.imread("estrela.jpg")
#print ("dados da imagem: ",img.shape)
altura=img.shape[0]
largura=img.shape[1]
canais=img.shape[2]

raio = input("Digite o valor do raio:")
raio2 = float(raio)**2
r=input("Digite o valor red: ")
g=input("digite o valor green: ")
b=input("Digite o valor blue: ")

for i in range(altura):
	for j in range(largura):
		dist=(float(img[i,j,2])-float(r))**2 + (float(img[i,j,1])-float(g))**2 + (float(img[i,j,0])-float(b))**2
		#print("dist = ",dist) #debug
		if (float(dist) < float(raio2)):
			img[i,j,2] = 255
			img[i,j,1] = 255
			img[i,j,0] = 255
		

cv2.imwrite("estrela-esfera.jpg",img)
cv2.imshow("Estrela esfera",img)
cv2.waitKey()
print("Imagem gerada com sucesso!")			


