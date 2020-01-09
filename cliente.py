# este archivo es prueba de recibir
import socket
import struct
import time
import csv

BUFFER = 1024  # tamanho del buffer
MSN = 'READY'
host = "192.168.1.2" # direccion ip
port = 6030


while True:
    s = socket.socket()
    s.connect((host, port))
    # recibimos la informacion enviada por el servidor
    ans = s.recv(BUFFER)
    # convertimos esa informacion a flotante

    print(ans)
    data =(struct.unpack('9f', ans))
    # imprimir la entrada en flotante
    print(data)
    s.close()
    # abrimos el archivo csv
    file = open('coordenadas.csv', 'a')
    # creamos el objeto lapiz para escribir
    lapiz = csv.writer(file)
    # escribimos el dato en el archivo csv
    lapiz.writerow(data)
    # cerramos el archivo csv
    file.close()
    time.sleep(5)