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

			              	ALGORITMO DE CONVULAÇÃO - TRABALHO II   
			              	        GUSTAVO GINO SCOTTON                                  
		""")

print("")
print("")
print("		Digite o nome e a extensão da imagem que deseja abrir para editar.")
print("		Exemplo: imagem.jpg ")
print("")
read= input("		Nome da imagem: ")
img = cv2.imread(read)

while True:
	print("""

				+--------------------------------------+
				|         Selecione uma Opção          |
				+--------------------------------------+

				+--------------------------------------+
				| [1] Identidade                       |
				+--------------------------------------+
				| [2] Detecção de Bordas / Objeto      |
				+--------------------------------------+
				| [3] Nitidez                          |
				+--------------------------------------+
				| [4] Desfocar                         |
				+--------------------------------------+
				| [5] Entalhar Imagem                  |
				+--------------------------------------+
				| [6] Inserir Matriz (Kernel)          |
				+--------------------------------------+
				| [7] Sair do programa                 |
				+--------------------------------------+

			        """)
	opcao = int(input("		Digite a opção escolhida: "))

	if (opcao ==1):
		kernel = np.array([[0,0,0],[0,1,0],[0,0,0]])

	elif (opcao ==2):
		print("""
				+--------------------------------------+
				|     Selecione o tipo de Detecção     |
				+--------------------------------------+

				+--------------------------------------+
				| [1] Detecção Baixa                   |
				+--------------------------------------+
				| [2] Detecção Média                   |
				+--------------------------------------+
				| [3] Detecção Alta                    |
				+--------------------------------------+
				| [4] Detecção Máxima                  |
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
		else:
			print("		A opção digitada não existe, por padrão escolhemos a primeira opção. (Detecção fraca)")
			kernel = np.array([[1,0,-1],[0,0,0],[-1,0,1]])	
	elif (opcao ==3):
		print("""
				+--------------------------------------+
				|     Selecione o tipo de Nitidez      |
				+--------------------------------------+

				+--------------------------------------+
				| [1] Nitidez Razoável                 |
				+--------------------------------------+
				| [2] Nitidez Máxima                   |
				+--------------------------------------+

			     """)	
		opcao2 = int(input("	Digite a opção escolhida: "))
		if (opcao2 == 1):
			kernel = np.array([[1,4,6,4,1], [4,16,24,16,4], [6,24,-476,24,6], [4,16,24,16,4], [1,4,6,4,1]])*(-1/256)
		elif (opcao2 == 2):
			kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
		else:
			print("		A opção digitada não existe, por padrão escolhemos a primeira opção. (Nitidez razoavel)")
			kernel = np.array([[1,4,6,4,1], [4,16,24,16,4], [6,24,-476,24,6], [4,16,24,16,4], [1,4,6,4,1]])*(-1/256)	
	elif (opcao ==4):
		print("""
				+--------------------------------------+
				|     Selecione o tipo de Desfoque     |
				+--------------------------------------+

				+--------------------------------------+
				| [1] Desfoque Baixo                   |
				+--------------------------------------+
				| [2] Desfoque Médio                   |
				+--------------------------------------+
				| [3] Desfoque Alto                    |
				+--------------------------------------+

				 """)	
		opcao2 = int(input("Digite a opção escolhida: "))
		if (opcao2 == 1):
			kernel = (np.array([[1,1,1],[1,1,1],[1,1,1]])/9)
		elif (opcao2 == 2):
			kernel = (np.array([[1,2,1],[2,4,2],[1,2,1]])/16)
		elif (opcao2 == 3):
			kernel = (np.array([[1,4,6,4,1], [4,16,24,16,4], [6,24,36,24,6], [4,16,24,16,4], [1,4,6,4,1]])/256)	
		else:
			print("		A opção digitada não existe, por padrão escolhemos a primeira opção. (Detecção fraca)")
			kernel = np.array([[1,0,-1],[0,0,0],[-1,0,1]])	
	elif (opcao == 5):
		kernel = np.array([[-2,-1,0],[-1,1,1],[0,1,2]])

	elif (opcao ==6):

		print("")
		print("		Matriz de convolução 3X3 : ")
		print("")
		v_11=float(input("	Digite o valor da posição [1,1] : "))
		v_12=float(input("	Digite o valor da posição [1,2] : "))
		v_13=float(input("	Digite o valor da posição [1,3] : "))
		v_21=float(input("	Digite o valor da posição [2,1] : "))
		v_22=float(input("	Digite o valor da posição [2,2] : "))
		v_23=float(input("	Digite o valor da posição [2,3] : "))
		v_31=float(input("	Digite o valor da posição [3,1] : "))
		v_32=float(input("	Digite o valor da posição [3,2] : "))
		v_33=float(input("	Digite o valor da posição [3,3] : "))
		v_div=float(input("	Digite o valor da divisão da Matriz : "))

		
		kernel = (np.array([[v_11,v_12,v_13],[v_21,v_22,v_23],[v_31,v_32,v_33]])/v_div)
			

	elif (opcao ==7):	
		print("")
		print("		Finalizando o programa...")
		sys.exit()
		cv2.destroyAllWindows()
		sys.exit()		

	else:
		print("")
		print("		------------------------------------------------------------------------")
		print("		-  Valor digitado não corresponde as opções, digite uma opção válida!  -")			
		print("		------------------------------------------------------------------------")
		print("")

	img_karnel = cv2.filter2D(img,-1,kernel) # Aplica o filtro de karnel na imagem
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
		print("	******************************************")
		print("	*   Digite qualquer tecla para fechar.   *")
		print("	******************************************")
		print("")
		cv2.imshow("Resultado da Imagem: "+str(read),img_karnel)
		cv2.waitKey()
		cv2.destroyAllWindows()
		img = img_karnel # Atualiza a img a ser editada, para poder realizar edição sobre edição.						
		