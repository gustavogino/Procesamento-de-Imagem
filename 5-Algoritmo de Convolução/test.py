import cv2
import numpy as np

img = cv2.imread("drhouse.jpg")


kernel = np.array([[0,0,0],[-0,1,0],[0,0,0]])/1 # Matriz de Kernel

img_karnel = cv2.filter2D(img,-1,kernel) # Aplica o filtro de karnel na imagem
	
cv2.imshow("Resultado da Imagem",img_karnel)
cv2.waitKey()
cv2.destroyAllWindows()