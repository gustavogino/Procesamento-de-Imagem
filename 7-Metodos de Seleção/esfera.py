import cv2
import numpy as np
import sys

print("Digite o nome e a extensão da imagem que deseja abrir para editar.")
print("Exemplo: imagem.jpg ")
read= input("Nome da imagem: ")
img = cv2.imread(read)

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
		

print("Como você gostaria de chamar esta imagem?")
print("Exemplo: Editada.jpg")
write = input("Nome da imagem: ")			

cv2.imwrite(write,img)
print("Imagem salva com sucesso!")	

resposta=input("Deseja visualizar a imagem agora? [Y] [N] : ")
if (resposta == "Y" or resposta=="y"):
	cv2.imshow("Exibição da Imagem",img)
	cv2.waitKey()
	cv2.destroyAllWindows()
	sys.exit()