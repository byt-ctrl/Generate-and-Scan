import cv2
from pyzbar.pyzbar import decode
import numpy as np

# Loading the image using 'OPENCV'
image=cv2.imread('QR Code.png')

# extracting the data from the QR Code 

decoded_objects=decode(image)
for obj in decoded_objects :
    print("Data --> ",obj.data.decode("utf-8"))  # Decoded DATA
    print("Type --> ",obj.type)

cv2.polylines(image,[np.array(obj.polygon,dtype=np.int32)],True,(0,0,255),3) # Drawing the polygon around the QR Code forn better visualization


# Displaying the QR code image scanning for showcasing use of OPEN CV
cv2.imshow("QR Code",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
