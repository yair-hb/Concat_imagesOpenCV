import cv2

imagen1 = cv2.imread('imagen_01.jpeg')
imagen2 = cv2.imread('imagen_02.jpeg')

print ('imagen1 shape=',imagen1.shape)
print ('imagen2 shape=',imagen2.shape)
concat_horizontal = cv2.hconcat([imagen1, imagen2])
concat_vertical = cv2.vconcat([imagen1,imagen2])

cv2.imshow('IMAGEN SALIDA hconcat', concat_horizontal)
cv2.imshow('IMAGEN SALIDA vconcat',concat_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()