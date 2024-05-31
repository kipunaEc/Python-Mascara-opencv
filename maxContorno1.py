import cv2
import numpy as np
lista_areas = []
img = cv2.imread("colibri.png")
img = cv2.blur(img, (5,5))
paisaje = cv2.imread("paisaje.png")
#Crear una imagen de color negro
alto, ancho, canales = img.shape
img2 = np.zeros((alto, ancho), np.uint8)
#Aplicando Canny
canny = cv2.Canny(img, 10, 100)
#Aplicar closing
kernel = np.ones((5,5))
closing = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
#Encontrar contornos
contornos, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#Dibujar los contornos
cv2.drawContours(img, contornos, -1, (0, 255, 0), 4)

for i in range(len(contornos)):
    area = cv2.contourArea(contornos[i])
    lista_areas.append(area)

area_max = max(lista_areas)
contornoMax = lista_areas.index(area_max)
cnt = contornos[contornoMax]
#cv2.drawContours(img, contornos, contornoMax, (0, 255, 0), 3)
cv2.drawContours(img2, [cnt], 0, 255, cv2.FILLED)

imgMascara1 = cv2.bitwise_and(img, img, mask = img2)
imgMascara2 = cv2.bitwise_and(paisaje, paisaje, mask =cv2.bitwise_not(img2))
imgFinal = cv2.add(imgMascara1, imgMascara2)

cv2.imshow("Contorno grande", img)
cv2.imshow("Imagen color B/N", img2)
cv2.imshow("imgMascara1", imgMascara1)
cv2.imshow("imgMascara2", imgMascara2)
cv2.imshow("Imagen Final", imgFinal)


cv2.waitKey(0)
cv2.destroyAllWindows()