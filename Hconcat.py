import cv2

imagen1 = cv2.imread('imagen_01.jpeg')
imagen2 = cv2.imread('imagen_02.jpeg')

#se imprimen los tmaños de las imagenes con sus canales
print ('imagen1 shape=',imagen1.shape)
print ('imagen2 shape=',imagen2.shape)

#se concatenan las imagenes de las formas que le indiquemos
concat_horizontal = cv2.hconcat([imagen1, imagen2])
concat_vertical = cv2.vconcat([imagen1,imagen2])

#concatenamos doble para generar un mosaico
concatx2 = cv2.hconcat([concat_horizontal, concat_horizontal])
concatx4 = cv2.vconcat([concatx2,concatx2])

cv2.imshow('IMAGEN SALIDA hconcat', concat_horizontal)
cv2.imshow('IMAGEN SALIDA vconcat',concat_vertical)
cv2.imshow('CONCAT X2',concatx2)
cv2.imshow('CONCAT X4',concatx4)
cv2.waitKey(0)
cv2.destroyAllWindows()