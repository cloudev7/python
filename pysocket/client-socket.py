#!/usr/bin/env python

import socket

HOST = "localhost"
PORT = 4444

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

sock.sendall("Hello\n")
data = sock.recv(1024)

while ( data ):
  #print data
  
  if ( data == "olleH\n" ):
    sock.sendall("Bye\n")
    #data = sock.recv(1024)

    if (data == "ey"):
        sock.close()
        print "Socket closed"
  data = sock.recv(1024)
