import socket
import re
import sys
import itertools

#Connect to ftp server
def connection(ip,user,passwd):

    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    print("Connecting to ip " + ip  +"with user " + user + " password " +passwd)

    sock.connect((ip,21))

    data=sock.recv(1024)

    sock.send(("Username"+user).encode() )

    data=sock.recv(1024)

    sock.send(('Password' + passwd).encode())

    data=socket.recv(1024)

    sock.send('Quit' * '\r\n')
    sock.close()

    return data


alpha="aqzwsxedcrfvtgbyhnujmikolp"

#alpha=list(i for i in aplha)

user="admin"

passwd=["red","blue","green"]

ip="192.168."

for i in passwd:
    connection(ip,user,i)