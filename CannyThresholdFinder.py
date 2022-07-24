import numpy as np
import cv2

def nothing():
    pass

cv2.namedWindow("Canny Threshold")
cv2.createTrackbar("Lower", "Canny Threshold", 20, 300, nothing)
cv2.createTrackbar("Upper", "Canny Threshold", 30, 300, nothing)

path = r"C:\Users\Kerem Ozben\Documents\GitHub\HairRootDetection\Samples\Sample1.jpeg"
img = cv2.imread(path)

while True:
    
    lower = cv2.getTrackbarPos("Lower", "Canny Threshold")
    upper = cv2.getTrackbarPos("Upper", "Canny Threshold")
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    #cont_bright = cv2.convertScaleAbs(gray, alpha = alpha, beta = beta)
    #gray = cv2.cvtColor(cont_bright, cv2.COLOR_BGR2GRAY)


    canny = cv2.Canny(blurred, alpha, beta)
    
    cv2.imshow("image", img)
    cv2.imshow("blurred", blurred)
    cv2.imshow("gray", gray)
    cv2.imshow("canny", canny)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

