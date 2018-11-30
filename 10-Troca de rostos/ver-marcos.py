from __future__ import division
import dlib
import cv2
import numpy as np



def redimensionar(img, largura=None, altura=None, funcao=cv2.INTER_AREA):
	global razao
	l, a = img.shape

	if largura is None and altura is None:
		return img
	elif largura is None:
		razao = altura / a	
		largura = int(l * razao)
		redimensionado = cv2.resize(img,(altura,largura),funcao)
		return redimensionado
	else:
		razao = largura / l
		altura = int(a * razao)
		redimensionado = cv2.resize(img, (altura, largura),funcao)
		return redimensionado



def transforma_np(ponto, dtype="int"):
	cordenada = np.zeros((68,2), dtype=dtype)
	for i in range(0, 68):
		cordenada[i] = (ponto.part(i).x, ponto.part(i).y)
	return cordenada	





ponto = None
camera = cv2.VideoCapture(0)
local_db = 'database/shape_predictor_68_face_landmarks.dat'
detector = dlib.get_frontal_face_detector()
database = dlib.shape_predictor(local_db)
i=0
#Dlib positions
#  ("mouth", (48, 68)),
#	("right_eyebrow", (17, 22)),
#	("left_eyebrow", (22, 27)),
#	("right_eye", (36, 42)),
#	("left_eye", (42, 48)),
#	("nose", (27, 35)),
#	("jaw", (0, 17))

while  True:
	on, frame = camera.read()
	if on == False:
		print("A captura de tela falhou. Por favor, cheque se a camera esta conectada! - Error in cv2.VideoCapture(0) \n")
		break

	frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	frame_redimensionado = redimensionar(frame_cinza, largura=120)	

	detec = detector(frame_redimensionado, 1)
	if len(detec) > 0:
		for k, d in enumerate(detec):
			ponto = database(frame_redimensionado, d)
			ponto = transforma_np(ponto)

			for (x, y) in ponto: # Mostra todos os pontos
				cv2.circle(frame, (int(x/razao), int(y/razao)), 3, (255, 255, 255), -1)


			#Código para brincar com os pontos
			cv2.circle(frame, (int(ponto[62,0]/razao), int(ponto[62,1]/razao)), 3, (0 ,0 ,255), -1)
			cv2.circle(frame, (int(ponto[66,0]/razao), int(ponto[66,1]/razao)), 3, (0 ,0 ,255), -1)
			


			p62= (ponto[62,0] + ponto[62,1])
			p66= (ponto[66,0] + ponto[66,1])
			dif_boca = (p66 - p62)
			#print("Distancia dos pontos: ",dif_boca)
			if (dif_boca > 1 or dif_boca <-1):
				print("A boca esta aberta!")
			else:
				print("A boca esta fechada!")

			"""				
			for w in range(0, 68):
				difp_vet.append(ponto[w,0] + ponto[w,1])
				print("Dif n"+str(w)+" -> "+str(difp_vet[w]))


				dif_boca = (difp_vet[65] - difp_vet[61])
			"""
	cv2.imshow("Detector de expressao",frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		camera.release()
		break
			






