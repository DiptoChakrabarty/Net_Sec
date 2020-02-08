import socket
import re
import sys

#Connect to ftp server
def connection(ip,user,passwd):

    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    print("Connecting to ip" + ip  +"with user " + user + "password " +passwd)

    sock.connect(('192.168.0.1',21))

    data=sock.recv(1024)

    sock.send("User"+user * '\r\n')

    data=sock.recv(1024)

    sock.send('Password' + passwd * '\r\n')

    data=socket.recv(1024)

    sock.send('Quit' * '\r\n')
    sock.close()

    return data


    