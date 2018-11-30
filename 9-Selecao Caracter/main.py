import cv2
import numpy as np

img = cv2.imread('j.png',0)


kernel = np.ones((5,5),np.uint8)
fino = cv2.erode(img,kernel,iterations = 1)
grosso = cv2.dilate(img,kernel,iterations = 1)
oco = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

while True:
	print("""

			+--------------------------------------+
			|         Selecione uma Opção          |
			+--------------------------------------+

			+--------------------------------------+
			| [1] Ver Original                     |
			+--------------------------------------+
			| [2] Afinar bordas                    |
			+--------------------------------------+
			| [3] Engrossar bordas                 |
			+--------------------------------------+
			| [4] Deixar imagem oca                |
			+--------------------------------------+
			| [5] Sair do programa                 |
			+--------------------------------------+

			        """)
	opcao = int(input("		Digite a opção escolhida: "))

	if (opcao ==1):
		cv2.imshow("Original ",img)
		cv2.waitKey()
		cv2.destroyAllWindows()

	elif (opcao ==2):
		cv2.imshow("Borda fina ",fino)
		cv2.waitKey()
		cv2.destroyAllWindows()

	elif (opcao ==3):
		cv2.imshow("Borda grossa ",grosso)
		cv2.waitKey()
		cv2.destroyAllWindows()

	elif (opcao ==4):
		cv2.imshow("Image oca ",oco)
		cv2.waitKey()
		cv2.destroyAllWindows()

	elif (opcao ==5):	
		print("")
		print("		Finalizando o programa...")
		sys.exit()
		cv2.destroyAllWindows()
		sys.exit()	
	else:
		print("Opção digitada não existe, tente novamente")		