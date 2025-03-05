# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 15:41:29 2025

@author:Seyda Nur
"""

import socket
from threading import Thread

Host='127.0.0.1'
Port=8080

clients={}
addresses={}

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((Host,Port))
def accept_client_connection():
    while True:
        client_conn,client_address=sock.accept()
        print(client_address,"Has connected")
        client_conn.send("Welcome to the chat room ,please Type Your Name To continue".encode('utf8'))
        Thread(target=handle_clients,args=(client_conn,client_address)).start()
def handle_clients(conn,address):
    name=conn.recv(1024).decode()
    welcome="Welcome "+name+". You can type #quit if you ever want to leave the chat room"
    
    conn.recv(bytes(welcome,"utf8"))
    msg=name+"Has recently joined the chat room"
    broadcast(bytes(msg,"utf8"))
    
    clients[conn]=name
    while True:
        msg=conn.recv(1024)
        if msg!=bytes("#quit","utf8"):
            broadcast(msg,name+" :")
        else:
            conn.send(bytes("#quit","utf8"))
            conn.close()
            del clients[conn]
            
            broadcast(bytes(name+"Has left the chat room"))
        
        ##addresses[client_conn]=client_address
def broadcast(msg,prefix=""):
    for x in clients:
        x.send(bytes(prefix,"utf8")+msg)
if __name__=="__main__":
    sock.listen(5)
    print("The server is running and is listening to clients requests")
    t1=Thread(target=accept_client_connection)
    t1.start()
    t1.join()
