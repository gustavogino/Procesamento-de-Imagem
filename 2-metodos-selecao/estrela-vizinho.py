import cv2
import numpy as np
import sys

img = cv2.imread("estrela.jpg")

altura=img.shape[0]
largura=img.shape[1]
canais=img.shape[2]

resp = "y"
while resp == "y" or resp=="Y":
	resp = input("Deseja adicionar um ponto? [Y] [N]")	
	if (resp == "n" or resp == "N"):
		print("Programa finalizado")
		cv2.imshow("Estrela Vizinho",img)
		cv2.waitKey()
		sys.exit()

	pred=input("Digite o ponto red: ")
	pgreen=input("Digite o ponto green: ")
	pblue=input("Digite o ponto blue: ")
	raio=input("Digite o raio: ")
	raio2=float(raio)**2

	for i in range(altura):
		for j in range(largura):
			distancia=(float(img[i,j,2])-float(pred))**2 + (float(img[i,j,1])-float(pgreen))**2 + (float(img[i,j,0])-float(pblue))**2
			#print("dist = ",dist) #debug
			if (float(distancia) < float(raio2)):
				img[i,j,2] = 255
				img[i,j,1] = 255
				img[i,j,0] = 255

	cv2.imwrite("estrela-vizinho.jpg",img)
	img =cv2.imread("estrela-vizinho.jpg")
	print("Ponto adicionado com sucesso!")			

	