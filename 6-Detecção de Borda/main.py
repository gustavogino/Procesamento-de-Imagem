import cv2
import numpy as np
import sys

print("""

			 _____                _                     _____  _____  _____ 
			|_   _|              (_)                   |_   _||_   _||_   _|
			  | |    ___   _ __   _   ___   ___   ___    | |    | |    | |  
			  | |   / _ \ | '_ \ | | / __| / _ \ / __|   | |    | |    | |  
			  | |  | (_) || |_) || || (__ | (_) |\__ \  _| |_  _| |_  _| |_ 
			  \_/   \___/ | .__/ |_| \___| \___/ |___/  \___/  \___/  \___/ 
			              | |                                               
			              |_|         

			              	ALGORITMO DE DETECÇÃO - TRABALHO III   
			              	        GUSTAVO GINO SCOTTON                                  
		""")

print("")
print("")
print("		Digite o nome e a extensão da imagem que deseja abrir para editar.")
print("		Exemplo: imagem.jpg ")
print("")
read= input("		Nome da imagem: ")
img = cv2.imread(read)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

while True:
	print("""
				+--------------------------------------+
				|     Selecione o tipo de Detecção     |
				+--------------------------------------+

				+--------------------------------------+
				| [1] Detecção Básica - Baixa          |
				+--------------------------------------+
				| [2] Detecção Básica - Média          |
				+--------------------------------------+
				| [3] Detecção Básica - Alta           |
				+--------------------------------------+
				| [4] Detecção Básica - Máxima         |
				+--------------------------------------+
				| [5] Detecção Avançada - Canny        |
				+--------------------------------------+
				| [6] Detecção Avançada - Sobel        |
				+--------------------------------------+
				| [7] Detecção Avançada - Prewitt      |
				+--------------------------------------+	
				| [8] Sair do programa                 |
				+--------------------------------------+			

	 """)	
	opcao2 = int(input("	Digite a opção escolhida: "))
	if (opcao2 == 1):
		kernel = np.array([[1,0,-1],[0,0,0],[-1,0,1]])


	elif (opcao2 == 2):
		kernel = np.array([[0,1,-0],[1,-4,1],[0,1,0]])


	elif (opcao2 == 3):
		kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])


	elif (opcao2 == 4):
		kernel = np.array([[-1.5,-1.5,-1.5],[-1.5,12,-1.5],[-1.5,-1.5,-1.5]])


	elif (opcao2 == 5):
		print("")
		print("		Digite os valores de intensidade de varedura nos eixos X e Y: ")
		print("")
		v=float(input("		Valor vertical (Y): "))
		h=float(input("		Valor horizontal (X): "))

		img_karnel = cv2.Canny(img,v,h) # Função para detecção de bordas OpenCV	 

	elif (opcao2 == 6):
		#sobel
		img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
		img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
		img_karnel = img_sobelx + img_sobely

	elif (opcao2 == 7):
		#prewitt
		kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
		kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
		img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
		img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
		img_karnel = img_prewittx + img_prewitty

	elif (opcao2==8):
		print("")
		print("		Finalizando o programa...")
		cv2.destroyAllWindows()
		sys.exit()	

	else:
		print("	Opção inválida!")
		print("")
		print("		Finalizando o programa...")
		cv2.destroyAllWindows()
		sys.exit()		
	
	if(opcao2 < 5):
		img_karnel = cv2.filter2D(img,-1,kernel) # Aplica o filtro de karnel na imagem
		img = img_karnel # Atualiza a img a ser editada, para poder realizar edição sobre edição.						
				
	print("")
	resposta=input("		Deseja salvar a imagem? [Y] [N] : ")
	if (resposta == "Y" or resposta=="y"):
		print("		Como você gostaria de chamar esta imagem?")
		print("		Exemplo: Editada.jpg")
		print("")
		write = input("Nome da imagem: ")
		cv2.imwrite(write,img_karnel)
		print("		Imagem salva com sucesso!")	
		print("")

	print("")	
	resposta=input("		Deseja visualizar a imagem agora? [Y] [N] : ")
	if (resposta == "Y" or resposta=="y"):
		print("")
		print("	***************************************************")
		print("	*   Digite qualquer tecla para fechar a imagem.   *")
		print("	***************************************************")
		print("")	
		cv2.imshow("Resultado da Imagem: "+str(read),img_karnel)
		cv2.waitKey()
		cv2.destroyAllWindows()
