# este archivo se ejecuta desde el servidor
import socket  # esta se usa para la transmision de datos mediante TCP/IP
import struct  # esta libreria es para convertir a bytes los datos a enviar
import csv  # esta se usa para manipular los archivos csv
import time

BUFFER = 1024
host = '192.168.1.2'
port = 6030  # puerto mayor a 5000
print(host)

def enviar_punto(p, cnn):
    """ esta funcion es la que envia las tres puntos via TCP/IP"""
    p_by = struct.pack('9f', p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8])
    cnn.send(p_by)

# estos son los puntos que vamos a enviar vis TCP/IP
point1 = [10, 20, 30]
point2 = [50, 5, 14]
point3 = [0, 0, 0]

# abrimos el csv en el que fueron escritos las coordenadas
f = open('coordenadas.csv', 'r+')
# vamos a escribir alguna informacion en formato csv
lapiz = csv.writer(f)

# abrimos el archivo historial de coordenadas
fsave = open("historial.csv", "a")
# vamos a crear un lapiz
lapizs = csv.writer(fsave)
# cargamos los puntos en data
data = point1[:]
for k in point2:
    data.append(k)
for k in point3:
    data.append(k)

# vamos a escribir los puntos en el csv
lapiz.writerows([point1, point2, point3])  # coordenadas.csv
lapizs.writerows([point1, point2, point3])  # historial.csv
f.close()
fsave.close()
# creamos el objeto socket
s = socket.socket()
# vinculamos el puerto con la direccion ip
s.bind((host, port))
# escuchamos hasta 5 clientes
s.listen(5)

while True:
    # aceptamos la peticion de conexion por parte del clientes
    cnn, addr = s.accept()
    print('nueva conexion establecida')
    print(addr)
    print(cnn)

    # llamamos a la funcion enviar_punto
    enviar_punto(data, cnn)

    # cerramos la conexion con el cliente
    cnn.close()
