import cv2
import numpy as np
import sys
import time

print("""

			 _____                _                     _____  _____  _____ 
			|_   _|              (_)                   |_   _||_   _||_   _|
			  | |    ___   _ __   _   ___   ___   ___    | |    | |    | |  
			  | |   / _ \ | '_ \ | | / __| / _ \ / __|   | |    | |    | |  
			  | |  | (_) || |_) || || (__ | (_) |\__ \  _| |_  _| |_  _| |_ 
			  \_/   \___/ | .__/ |_| \___| \___/ |___/  \___/  \___/  \___/ 
			              | |                                               
			              |_|         

			              	ALGORITMO DE SEGMENTAÇÃO - TRABALHO IV  
			              	        GUSTAVO GINO SCOTTON                                  
		""")

print("")
print("")
print("		Digite o nome e a extensão da imagem que deseja abrir para editar.")
print("		Exemplo: imagem.jpg ")
print("")
read= input("		Nome da imagem: ")
#read = 'cor.jpg'
img = cv2.imread("input/"+read)

print("")
K= int(input("		Quantidade de cores que deseja como saída: "))
print("")
print("	> Abrindo imagem...")	
#time.sleep(1.5)

#Aplica filtro gaussiano pra suavizar a imagem e detectar melhor
img_gaussian = cv2.GaussianBlur(img,(3,3),0)
img_float = img_gaussian.reshape((-1,3))
print("		> Aplicando filtro...")
#time.sleep(1.5)

# converte pra numpy float32 para realizar as operações
img_float = np.float32(img_float)
print("			> Convertento para numérico...")
#time.sleep(1.5)

# define critérios e aplica a função cv2.kmeans()
criterio = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
dist,omega,img_centro = cv2.kmeans(img_float, K, None, criterio, 10, cv2.KMEANS_RANDOM_CENTERS)
print("				> Agrupando cores...")
#time.sleep(1.5)

# Agora converte de volta para uint8, transformando em formato imagem
img_centro = np.uint8(img_centro)
print("					> Convertendo para imagem...")
#time.sleep(1.5)
resultado = img_centro[omega.flatten()]
resultado = resultado.reshape((img.shape))

print("						> Resultado finalizado!")	
#time.sleep(1)
print("")

#Oferece opção para salvar a imagem na pasta "results"

resposta=input("		Deseja salvar a imagem? [Y] [N] : ")
if (resposta == "Y" or resposta=="y"):
	print("		Como você gostaria de chamar esta imagem?")
	print("		Exemplo: Editada.jpg")
	print("")
	write = input("Nome da imagem: ")
	cv2.imwrite("results/"+write, resultado)
	print("		Imagem salva com sucesso na pasta 'results'!")	
	print("")
print("")	

#Oferece opção para visualizar a imagem
resposta=input("		Deseja visualizar a imagem agora? [Y] [N] : ")
if (resposta == "Y" or resposta=="y"):
	print("")
	print("	***************************************************")
	print("	*   Digite qualquer tecla para fechar a imagem.   *")
	print("	***************************************************")
	print("")	
	cv2.imshow("Resultado da Imagem: "+str('read'),resultado)
	cv2.waitKey()
	cv2.destroyAllWindows()
