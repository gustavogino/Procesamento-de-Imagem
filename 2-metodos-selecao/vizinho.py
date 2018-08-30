import cv2
import numpy as np
import sys

print("Digite o nome e a extensão da imagem que deseja abrir para editar.")
print("Exemplo: imagem.jpg ")
read= input("Nome da imagem: ")
img = cv2.imread(read)
img2 = cv2.imread(read)

altura=img.shape[0]
largura=img.shape[1]
canais=img.shape[2]

resp = "y"
while resp == "y" or resp=="Y":
	resp = input("Deseja adicionar um ponto? [Y] [N]")	
	if (resp == "n" or resp == "N"):
		print("Como você gostaria de chamar esta imagem?")
		print("Exemplo: Editada.jpg")
		write = input("Nome da imagem: ")			

		cv2.imwrite(write,img)
		print("Imagem salva com sucesso!")	

		resposta=input("Deseja visualizar a imagem agora? [Y] [N] : ")
		if (resposta == "Y" or resposta=="y"):
			print("Digite qualquer tecla para fechar.")
			cv2.imshow("Exibição da Imagem",img)
			cv2.waitKey()
			cv2.destroyAllWindows()
		print("Finalizando o programa...")	
		sys.exit()
	img=img2
	pred=input("Digite o ponto [RED]: ")
	pgreen=input("Digite o ponto [GREEN]: ")
	pblue=input("Digite o ponto [BLUE]: ")
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

	img2=img
	print("Ponto adicionado com sucesso!")	