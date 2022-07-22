import numpy as np
import cv2

def nothing():
    pass

def DrawHairs (img, hairs):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for hair in hairs:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1,y1), (x2,y2), (0, 255, 0), thickness=10)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

cv2.namedWindow("Contrast-Brightness")
cv2.createTrackbar("Alpha", "Contrast-Brightness", 100, 300, nothing)
cv2.createTrackbar("Beta", "Contrast-Brightness", 0, 100, nothing)


#alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
#beta = int(input('* Enter the beta value [0-100]: '))

path = r"C:\Users\Kerem Ozben\Documents\GitHub\HairRootDetection\Samples\Sample1.jpeg"
img = cv2.imread(path)
while True:
    alpha = float(cv2.getTrackbarPos("Alpha", "Contrast-Brightness")/100)
    beta = cv2.getTrackbarPos("Beta", "Contrast-Brightness")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    enhance = cv2.equalizeHist(gray)
    thresh = 90
    im_bw = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]
    cont_bright = cv2.convertScaleAbs(img, alpha = alpha, beta = beta)
    gray = cv2.cvtColor(cont_bright, cv2.COLOR_BGR2GRAY)


    canny = cv2.Canny(gray, 100, 250)
    canny_bw = cv2.Canny(im_bw, 100, 250)

    cv2.imshow("image", img)
    cv2.imshow("CONTRAST", cont_bright)
    cv2.imshow("gray", gray)
    #cv2.imshow("enhance", enhance)
    #cv2.imshow("canny", canny)
    #cv2.imshow("binary", im_bw)
    #cv2.imshow("canny_bw", canny_bw)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

