import cv2
import numpy as np
import sys
from numpy.linalg import inv

while True:
	i=0
	j=0

	print("""
		+--------------------------------------+
		|         Selecione uma Opção          |
		+--------------------------------------+

		+--------------------------------------+
		| [1] Seleção cuboide                  |
		+--------------------------------------+
		| [2] Seleção esférica                 |
		+--------------------------------------+
		| [3] Distância de Mahalanobis         |
		+--------------------------------------+
		| [4] Distância K-Vizinhos             |
		+--------------------------------------+
		| [5] Sair do programa                 |
		+--------------------------------------+

	            """)
	opcao = int(input("Digite a opção escolhida: "))

	if (opcao ==1): #######################################################################################################################

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
			print("Digite qualquer tecla para fechar.")
			cv2.imshow("Imagem",img)
			cv2.waitKey()
			cv2.destroyAllWindows()

	elif (opcao ==2):	#######################################################################################################################

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
			print("Digite qualquer tecla para fechar.")
			cv2.imshow("Imagem",img)
			cv2.waitKey()
			cv2.destroyAllWindows()

	elif (opcao ==3):	#######################################################################################################################

		print("Digite o nome e a extensão da imagem que deseja abrir para editar.")
		print("Exemplo: imagem.jpg ")
		read= input("Nome da imagem: ")
		img = cv2.imread(read)

		altura=img.shape[0]
		largura=img.shape[1]
		canais=img.shape[2]


		m=[0]*3
		w=int(0)
		nponto = int(input("Quantos pontos você deseja introduzir? "))
		raiooo = float(input("Qual o tamanho do raio que deseja? "))
		vred=[0]*nponto
		vgreen=[0]*nponto
		vblue=[0]*nponto

		for w in range(nponto):
			pred=input("Digite o ponto nº: "+str(w)+" [RED] ")
			pgreen=input("Digite o ponto nº: "+str(w)+" [GREEN] ")
			pblue=input("Digite o ponto nº: "+str(w)+" [BLUE] ")
			vred[w]=float(pred)
			vgreen[w]=float(pgreen)
			vblue[w]=float(pblue)
			m[0] = float(m[0])+float(vred[w])
			m[1] = float(m[1])+float(vgreen[w])
			m[2] = float(m[2])+float(vblue[w])
					
		m[0] = m[0] / float(nponto)
		m[1] = m[1] / float(nponto)
		m[2] = m[2] / float(nponto)

		m_cov=np.zeros((3,3), dtype=np.float64)
		z=int(0)
		for z in range(nponto):
			m_cov[0,0]= ((vred[z]-m[0])*(vred[z]-m[0])) + m_cov[0,0]
			m_cov[1,0]= ((vred[z]-m[0])*(vgreen[z]-m[1])) + m_cov[1,0]
			m_cov[2,0]= ((vred[z]-m[0])*(vblue[z]-m[2])) + m_cov[2,0]
			m_cov[2,1]= ((vgreen[z]-m[1])*(vblue[z]-m[2])) + m_cov[2,1]
			m_cov[1,1]= ((vgreen[z]-m[1])*(vgreen[z]-m[1])) + m_cov[1,1]
			m_cov[2,2]= ((vblue[z]-m[2])*(vblue[z]-m[2])) + m_cov[2,2]

		m_cov[0,2]= m_cov[2,0]
		m_cov[1,2]= m_cov[2,1]
		m_cov[0,1]= m_cov[1,0] 

		n=float(nponto)
		i = int(0)
		j = int(0)
		for i in range(2):
			for j in range(2):
				m_cov[i,j]= (m_cov[i,j] / n)
		i_cov = inv(m_cov)
		vet=[0]*3
		for g in range(altura):
			for f in range(largura):
				vet[0]=float(img[g,f,2])-float(m[0])
				vet[1]=float(img[g,f,1])-float(m[1])
				vet[2]=float(img[g,f,0])-float(m[2])
				tvet=np.transpose(vet)
				aux = np.dot(i_cov,vet)
				dist=np.dot(tvet,aux)
				d=float(dist)
				if(d < raiooo):
					#print("D: ",d)
					img[g,f,2] = 255
					img[g,f,1] = 255
					img[g,f,0] = 255



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


	elif (opcao ==4):	#######################################################################################################################
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
		backup=cv2.imread(read)
		altura=img.shape[0]
		largura=img.shape[1]

		raio=input("Digite o raio a ser definido: ")
		raio2=float(raio)**2

		print("Clique na imagem no ponto em que deseja excluir.")
		print("ESC para finalizar    |   Espaço para restaurar ")
		cv2.namedWindow("Manipulando a Imagem : "+str(read))
		cv2.setMouseCallback("Manipulando a Imagem : "+str(read),kvizinho)
		#Do until esc pressed
		bolean=True
		while(bolean):
			cv2.imshow("Manipulando a Imagem : "+str(read),img)
			if cv2.waitKey(20) & 0xFF == 32:
				img=backup
				print(" ")
				print("Imagem restaurada!")
				print(" ")
			elif cv2.waitKey(20) & 0xFF == 27:
				bolean = False
				cv2.destroyAllWindows()
				sel=input("Deseja salvar a imagem? [Y] [N] : ")
				if (sel=='Y' or sel=='y'):			
					print("Digite o nome de como deseja salvar (não necessita extensão)")
					print("Exemplo: Imagem-nova")
					write=input("Nome da imagem: ")
					cv2.imwrite(write,img)
					print("Imagem salva com sucesso!")
	

	elif (opcao ==5):	#######################################################################################################################
		print("Finalizando o programa...")
		cv2.destroyAllWindows()
		sys.exit()
	else:
		print("A opção informada não existe, digite novamente!")	