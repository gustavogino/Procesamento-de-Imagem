import cv2
import numpy as np
import sys

count = int(0)
def kvizinho(event,x,y,flags,param):
	global count
	altura=img.shape[0]
	largura=img.shape[1]
	if (event == cv2.EVENT_LBUTTONDOWN): 
		count=int(count+1)
		pblue = float(img[y,x,0])
		pgreen = float(img[y,x,1])
		pred = float(img[y,x,2])
		colors = img[y,x]
		print(" ")
		print("Ponto Red: ",pblue)
		print("Ponto Green: ",pgreen)
		print("Ponto Blue: ",pred)
		print("Coordenadas do Pixel: X: ",x,"Y: ",y)
		print("Ponto nº "+str(count)+" foi adicionado com raio : "+str(raio)+" !")
		print(" ")
		for i in range(altura):
			for j in range(largura):
				distancia=(float(img[i,j,2])-float(pred))**2 + (float(img[i,j,1])-float(pgreen))**2 + (float(img[i,j,0])-float(pblue))**2
				if (float(distancia) < float(raio2)):
					img[i,j,2] = 255
					img[i,j,1] = 255
					img[i,j,0] = 255

print("Digite o nome e a extensão da imagem que deseja abrir para editar.")
print("Exemplo: imagem.jpg ")
read= input("Nome da imagem: ")

img = cv2.imread(read)
altura=img.shape[0]
largura=img.shape[1]

raio=input("Digite o raio a ser definido: ")
raio2=float(raio)**2

print("Clique na imagem no ponto em que deseja excluir.")
print("ESC para finalizar")
cv2.namedWindow("Manipulando a Imagem : "+str(read))
cv2.setMouseCallback("Manipulando a Imagem : "+str(read),kvizinho)
#Do until esc pressed
bolean=True
while(bolean):
	cv2.imshow("Manipulando a Imagem : "+str(read),img)
	if cv2.waitKey(20) & 0xFF == 27:
		bolean = False
		cv2.destroyAllWindows()
		sel=input("Deseja salvar a imagem? [Y] [N] : ")
		if (sel=='Y' or sel=='y'):			
			print("Digite o nome de como deseja salvar (não necessita extensão)")
			print("Exemplo: Imagem-nova")
			write=input("Nome da imagem: ")
			cv2.imwrite(write,img)
			print("Imagem salva com sucesso!")
