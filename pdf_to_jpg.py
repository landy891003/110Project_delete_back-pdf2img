from pdf2image import convert_from_path
from PIL import Image 
import os
import PIL 

num=[]
f=open("number.csv","r")
numbers=f.readlines()
for number in numbers:
    list=number.split(", \n")
    num.append(list[0])
f.close()
print(len(num))
n=0
i=0
while(n<len(num)):
    try:
        heart_path="C:\\Users\\USER\\Desktop\\heart\\heart_diagram\\heart_pic_pre\\EKG_"+num[n]+"_pre.pdf"
        pages = convert_from_path(heart_path,fmt='jpeg',poppler_path = r"C:\\Users\\USER\\Desktop\\Python 3.9\\poppler-21.03.0\\Library\\bin")
        pages[0].save("C:\\Users\\USER\\Desktop\\heart\\heart_diagram\\heart_pre\\"+num[n]+'_pre.jpg','JPEG')
        print(num[n],"次數:",i)
        i=i+1
    except Exception as e:
        print(num[n],e)
    n=n+1
f.close()
        
