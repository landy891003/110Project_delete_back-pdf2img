import numpy as np
import cv2
import os
f=open("number.csv","r")
numbers=f.readlines()
num=[]
for number in numbers:
    list=number.split(",")
    num.append(list[0])
f.close()

redLower = np.array([0, 0, 0])
redUpper = np.array([180, 255, 46])
n=0
i=0
while n<len(num):
    try:
        image = 'C:\\Users\\USER\\Desktop\\heart\\heart_diagram\\heart_pre\\'+num[n]+'_pre.jpg'     #修改此處
        img = cv2.imread(image)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, redLower, redUpper)
        mask1 = cv2.bitwise_not(mask,mask)
        cv2.imwrite('C:\\Users\\USER\\Desktop\\heart\\heart_diagram\\heart_pre\\'+num[n]+'_pre.jpg', mask1) #修改此處
        cv2.waitKey(0)
        print(num[n],"finished delete back",i)
        i=i+1
    except Exception as e:
        print(num[n],e)
    n=n+1

