#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys
import os


class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write("Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print "El cliente nos manda " + line
            method = line.split(" ")[0]
            if method == "INVITE":
                self.wfile.write("SIP/2.0 100 Trying\r\n")
                self.wfile.write("SIP/2.0 180 Ring\r\n")
                self.wfile.write("SIP/2.0 200 OK\r\n")
            elif method == "ACK":
                aEjecutar = ('mp32rtp -i ' + IP + ' -p 23032 < ' + fichero_audio)
                print "Vamos a ejecutar", aEjecutar
                os.system(aEjecutar) 
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer(("", 6001), EchoHandler)
    print "Lanzando servidor UDP de eco..."
    serv.serve_forever()
