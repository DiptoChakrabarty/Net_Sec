import socket
import re
import sys
import itertools

#Connect to ftp server
def connection(ip,user,passwd):

    #sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock= socket.socket()

    print("Connecting to ip " + ip  +"with user " + user + " password " +passwd)

    sock.connect((ip,21))
    

    print("Connected")

    data=sock.recv(1024).decode()
    print(data)

    sock.send(("Username:"+user).encode() )
    print("Username")
    print(data)

    data=sock.recv(1024).decode()

    sock.send(('Password' + passwd).encode())
    print("Password")
    print(data)

    data=socket.recv(1024).decode()

    sock.send(('Quit').encode())
    print("Quit")
    sock.close()

    return data


alpha="aqzwsxedcrfvtgbyhnujmikolp"

#alpha=list(i for i in aplha)

user="admin"

passwd=["red","blue","green"]

ip="192.168"

for i in passwd:
    print(connection(ip,user,i))