import cv2
import imutils

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret,frame=cap.read()
    if ret == False:
        break

    gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(gray,100,255, cv2.THRESH_BINARY)

    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    th = cv2.cvtColor(th, cv2.COLOR_GRAY2BGR)
    gray = imutils.resize(gray, height=(gray.shape[0]//2))
    th = imutils.resize(th, height=(th.shape[0]//2))
    
    concatV = cv2.vconcat([gray,th])
    concatH = cv2.hconcat([frame, concatV])

    cv2.putText(concatH,'VIDEO STREAMING',(10,20),1,1.5,(0,255,0),2)
    cv2.putText(concatH,'ESCALA DE GRISES',(650,20),1,1.5,(0,255,0),2)
    cv2.putText(concatH,'BINARIZADA',(650,260),1,1.5,(0,255,0),2)

    cv2.imshow('concatH', concatH)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()