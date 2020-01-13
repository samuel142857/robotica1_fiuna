# este script se usa para sacar fotos con la webcam
import cv2 as cv

camara = cv.VideoCapture(2) # el puerto de la camara integrada a la computadora es 0, al conectar a los puertos usb, hay que empezar a buscar desde 1
i = 0
while True:
    ret, frame = camara.read()
    cv.imshow('imagen', frame)
    if cv.waitKey(1) & 0xFF == ord('f'):
        retu, imagen = camara.read()  # captura video cuadro a cuadro, devuelve un boot si es que el cuadro se lee correctamente
        cv.imwrite('foto'+str(i)+'.png', imagen)
        i += 1
    elif cv.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv.destroyAllWindows()
