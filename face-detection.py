# chapter - 9 ////  Face detection

import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('****.jpg')                                    # **=image file
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(grayimg,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,144,201),2)

cv2.imshow('detected',img)
cv2.waitKey(0)
