#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys


# Cliente UDP simple.
method = sys.argv[1]
cliente = sys.argv[2]

# Dirección IP del servidor.

if len(sys.argv) =! 3:
    sys.exit("Usage: python client.py method receiver@IP:SIPport")
#ACK no lo introduce el usuario
if method != "INVITE" or "BYE":
    sys.exit("Usage: python client.py method receiver@IP:SIPport")
if ":" or "@" not in cliente:
    sys.exit("Usage: python client.py method receiver@IP:SIPport")
receptor = cliente.split("@")[0]
cliente = cliente.split("@")[1]

SERVER = cliente.split(":")[0]
PORT = int(cliente.split(":")[1])

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))
LINE = method + " sip:" + receptor + "@" + SERVER + " SIP/2.0"
print "Enviando: " + LINE
my_socket.send(LINE + '\r\n')
try:
    data = my_socket.recv(1024)
except socket.error:
    print  "Error: no server listening at" + SERVER + " port " + str(PORT)
    sys.exit()

print 'Recibido -- ', data
response = data.split("SIP/2.0 ")
if response[1] ==    
print "Terminando socket..."
# Cerramos todo
my_socket.close()
print "Fin."
