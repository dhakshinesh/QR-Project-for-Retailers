import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)



with open("mydatafile.txt") as f:
    mydatalist = f.read().splitlines()
print(mydatalist)

while True:

    success,img = cap.read()

    for barcode in decode(img):
        mydata = barcode.data.decode('utf-8')
        print(mydata)

        if mydata in mydatalist:
            myoutput = "Authorized"
            mycolor = (0,0,255)
        else:
            myoutput = "Un-Authorized"
            mycolor = (255,0,0)

        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,mycolor,5)

    cv2.imshow('Result',img)
    cv2.waitKey(1)
