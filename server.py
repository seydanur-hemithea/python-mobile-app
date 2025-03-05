# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 16:53:09 2025

@author: Seyda Nur
"""
import socket

host='localhost'
port=8080
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((host,port))
sock.listen(1)
print("the server is running and is listening to clients requests ")

conn, address =sock.accept()
print("Coonnection has been established with",str(address))

"""message="Hey there is something important for you"

##message 

conn.send(message.encode())"""
try:
    fileName=conn.recv(1024)##dosya
    file=open(fileName,'rb')
    readFile=file.read()
    conn.send(readFile)
    
    file.close()
except:
    conn.send("file not found on the server".encode())
    


conn.close()