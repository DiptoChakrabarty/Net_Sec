import socket
import struct
import textwrap

#Unpack etehrnet packet

def ether_frame(data):
    dest_mac,src_mac,proto=struct.unpack('!',)