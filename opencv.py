# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:48:37 2025

@author: Seyda Nur
"""

import cv2

img=cv2.imread('lena_bw.png',-1)
img=cv2.line(img,(0,0),(255,255),(0,255,0),5)#resmin uzerine ciczgi cizdik
img=cv2.arrowedLine(img,(0,255),(255,255),(0,0,255),10)
img=cv2.rectangle(img, (255,0),(500,100), (0,0,255),-1)#sekil cizme
img=cv2.circle(img, (300,200), 60, (0,255,255),5)
font=cv2.FONT_HERSHEY_DUPLEX

img=cv2.putText(img, "beautiful lena", (1,200), font, 4, (0,0,255),10,cv2.LINE_AA)

cv2.imshow("lena",img)
key=cv2.waitKey(5000)
if key==27:    
   cv2.destroyAllWindows()
if key==ord("s"):
    cv2.imwrite("beautiful lena.png",img)
    cv2.destroyAllWindows()
#%%
import cv2
import datetime
cap=cv2.VideoCapture(0)#camera adı yazilabilir
fourcc=cv2.VideoWriter_fourcc(*'XVID')
output=cv2.VideoWriter('Register.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret,frame=cap.read()
    output.write(frame)
    print("Frame Width before setting",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print("Frame Height before setting",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if ret==True:
        font=cv2.FONT_HERSHEY_SIMPLEX
        text="Width:" + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + "height:"+ str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        dT=str(datetime.datetime.now())
        frame=cv2.putText(frame,dT,(10,20),font,1,(0,0,255),2,cv2.LINE_AA)
       # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#groruntu griyecevrilir
        cv2.imshow('Video Frame',frame)
        
        
        if cv2.waitKey(1)==ord('q'):
            break
cap.release()
output.release() 
cv2.destroyAllWindows() 
   