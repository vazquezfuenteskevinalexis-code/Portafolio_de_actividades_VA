"""
OCR=OPTICAL CHARACTER RECOGNITION/RECONOCIMIENTO
OPTICO DE CARACTERES
POR EJEMPLO:
-FOTO DE UN DOCUMENTO
-DOCUMENTO ESCANEADO
-UN RECIBO
-SEÑAL CON LETRAS, UNA FOTO BIEN ENFOCADA

¿QUE HACE?=RECONOCE LAS FORMAS DE LAS LETRAS Y
CONVIERTE A TEXTO DIGITAL EDITABLE/COPIABLEmanipular
import pytesseract #
"""
#C:\Users\MATUTINO\AppData\Local\Programs\Tesseract-OCR

import cv2 #Importa Pythoncv para manipular
import pytesseract #Libreria OCR

pytesseract.pytesseract.tesseract_cmd=r"C:\Users\MATUTINO\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

#Cargar la imagen
img_texto=cv2.imread("TEXTO_1.webp")

#Redimensionar el tamaño de la imagen
img_final=cv2.resize(img_texto,(800,400))

#Convertir a escala de grises
img_gris=cv2.cvtColor(img_final,cv2.COLOR_BGR2GRAY)
#Separamos el fondo con el texto
img_res=cv2.threshold(img_gris,120,255,cv2.THRESH_BINARY)[1]
#Devuelve dos valores, los pixeles y la imagem procesada

#Configurar OCR
texto=pytesseract.image_to_string(img_res,lang="es")
#Cmomo parametro la pasamos la variable con la imagen procesada y el idioma
#Imprimimos el titulo
print("Texto detectado")
print(texto)

cv2.imshow("Imagen analizada",img_final)
cv2.waitKey(0)
cv2.destroyAllWindows()