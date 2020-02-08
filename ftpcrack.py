import socket
import re
import sys

#Connect to ftp server
def connection(ip,user,passwd):

    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    print("Connecting to ip" + ip  +"with user " + user + "password " +passwd)