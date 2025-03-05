# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 17:02:35 2025

@author: Seyda Nur
"""

import socket
host='localhost'
port=8080
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


sock.connect((host,port))
"""
message=sock.recv(1024)

while message:
    print("Message:",message.decode())
    message=sock.recv(1024)"""##•mesaj 


fileName='abc.txt'##dosya
sock.send(fileName.encode())    
readFile=sock.recv(1024)
print(readFile.decode())
sock.close()