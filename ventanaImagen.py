#Librería
import cv2  #clase estatica
from cv2 import imshow  #de la clase cv2 que traiga el metodo imshow
"""import pytesseract
tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'"""

imgText="cafe" #variable que guarda el nombre de la imagen
#Lectura de imagen
img= cv2.imread(imgText+'.png') 
'''
img  => la variable que va a guardar la informacion que ejecuta el metodo
cv2.imread(imgText+'.png')  => cv2.imread => metodo para leer imagen en cualquier formato
                            => (imgText+'.png') => llama la variable donde se guardo el nombre 
                                                de la imagen y lo concatena con el tipo del 
                                                formato de la imagen 
'''
imshow('Imagen Original',img)
'''
imshow  => permite la visualización de la imagen
        => metodo imshow de la libreria cv2
('Imagen Original',img) => ('nombre de la ventana', parametro: la variable en donde se muestra)
'''
img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
'''
cvtColor => se utiliza para convertir una imagen de un espacio de color a otro.

Sintaxis: cv2.cvtColor(origen, código[, dst[, dstCn]])

Parámetros:
src: Es la imagen cuyo espacio de color se desea modificar.
código: Es el código de conversión del espacio de color.
dst: es la imagen de salida del mismo tamaño y profundidad que la imagen src. Es un parámetro opcional.
dstCn: Es el número de canales en la imagen de destino. Si el parámetro es 0, el número de canales se deriva automáticamente de src y código. Es un parámetro opcional.

Valor devuelto: Devuelve una imagen.
'''
cv2.imshow('Imagen Gris', img_gris)

r = img.copy() #metodo para replicar la imagen
r[:, :, 0] = 0 #=> [posicionx,posiciony,color rojo] = 0 tonalidad
r[:, :, 1] = 0 #=> [posicionx,posiciony,color rojo] = 0 tonalidad
cv2.imshow('R-RGB', r)

g = img.copy()
g[:, :, 0] = 0
g[:, :, 2] = 0
cv2.imshow('G-RGB', g)

b = img.copy()
b[:, :, 1] = 0
b[:, :, 2] = 0
cv2.imshow('B-RGB', b)
########################################################################################
cv2.waitKey(0)
'''
cv2.waitKey => espera a que el usuario presione cualquier tecla para cerrar la pestaña
            => metodo waitKey de la libreria cv2
            => esto es necesario para evitar que el kernel de Python se cuelgue
(0)    => evita que la pestaña se cierre
'''
cv2.destroyAllWindows()
'''
cv2.destroyAllWindows() => termina la ejecucion del programa y cierra todas las ventanas
                        => metodo destroyAllWindows() de la libreria cv2
'''