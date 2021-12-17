import cv2
import imutils as im

imagen1 = cv2.imread('imagen_01.jpeg')
imagen2 = cv2.imread('imagen_02.jpeg')
imagen3 = cv2.imread('ave.jpg')
imagen3 = im.resize(imagen3, width=600)

#imprime las dimnesiones de las imagens a concatenar
print('shape imagen1=',imagen1.shape)
print('shape imagen2=',imagen2.shape)
print('shape imagen3=',imagen3.shape)

#conactenando una imagen arriba y dos abajo
concatx3 = cv2.hconcat([imagen1,imagen2,imagen1])
concatx4 = cv2.vconcat([imagen3,concatx3])

cv2.imshow('IMAGENES CONCATENADAS', concatx4)
cv2.waitKey(0)
cv2.destroyAllWindows()