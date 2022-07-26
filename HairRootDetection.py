import numpy as np
import cv2

def nothing(): ## boş fonksiyon
    pass

def DrawHairs (img, hairs): # Saç köklerini çizen fonksiyon
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for hair in hairs:
        for x1, y1, x2, y2 in hair:
            cv2.line(blank_image, (x1,y1), (x2,y2), (0, 255, 0), thickness=1)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

## Arayüz penceresi
cv2.namedWindow("Canny Threshold")
cv2.createTrackbar("Lower", "Contrast-Brightness", 47, 300, nothing)
cv2.createTrackbar("Upper", "Contrast-Brightness", 73, 300, nothing)
##

path = r"C:\Users\Kerem Ozben\Documents\GitHub\HairRootDetection\Samples\Sample1.jpeg" ## Fotoğrafın olduğu path
img = cv2.imread(path) ## fotoğrafı okuma

while True:
    alpha = cv2.getTrackbarPos("Lower", "Contrast-Brightness") ## arayüzden değer okuma
    beta = cv2.getTrackbarPos("Upper", "Contrast-Brightness")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # grayscale geçme
    blurred = cv2.GaussianBlur(gray, (7, 7), 0) # blur uygulama

    #cont_bright = cv2.convertScaleAbs(gray, alpha = alpha, beta = beta) # parlaklık kontrast ayarlama
    #gray = cv2.cvtColor(cont_bright, cv2.COLOR_BGR2GRAY)


    canny = cv2.Canny(blurred, alpha, beta) # Canny kenar tespiti
    hairs = cv2.HoughLinesP(canny, 1, np.pi/180, 0) # Hough çizgi tespiti
    print(hairs)

    img_withHairs = DrawHairs(img, hairs) # Fonksiyon ile çizgiler çizilir.


    cv2.imshow("image", img)
    cv2.imshow("blurred", blurred)
    cv2.imshow("gray", gray)
    cv2.imshow("canny", canny)
    cv2.imshow("img_withHairs", img_withHairs)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

