import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm


pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
dectetor= htm.handdectetor()

while True:
	success, img = cap.read()

	img=dectetor.findhands(img)

	lmList=dectetor.finposition(img, draw=False)
	if len(lmList) !=0:
		print(lmList)

		fingures = dectetor.fingersup()
		print(fingures)





	cTime=time.time()
	fps = 1/(cTime-pTime)
	pTime = cTime


	cv2.putText(img, str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,3, (255,0,255),3)
	cv2.imshow("image",img)
	cv2.waitKey(1)