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
red = float(input("Digite o valor máximo [RED]: "))
red1 = float(input("Digite o valor minímo [RED]: "))
green = float(input("Digite o valor máximo [GREEN]: "))
green1 = float(input("Digite o valor minímo [GREEN]: "))
blue = float(input("Digite o valor máximo [BLUE]: "))
blue1 = float(input("Digite o valor minímo [BLUE]: "))

for i in range(altura):
	for j in range(largura):
		if ( (float(img[i,j,2]) < red) and (float(img[i,j,2])  > red1) and (float(img[i,j,1]) < green) and (float(img[i,j,1]) > green1)  and (float(img[i,j,0]) < blue) and (float(img[i,j,0]) > blue1) ):

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
	print("Finalizando o programa...")
	sys.exit()
print("Finalizando o programa...")	