import socket
import struct
import textwrap

#Unpack etehrnet packet

def ether_frame(data):
    dest_mac,src_mac,proto=struct.unpack('! 6s 6s H',data[:14])
    return get_mac_addr(dest_mac),get_mac_addr(src_mac),socket.htons(proto),data[:14]
# Obtain Mac Addresses from data 

# Make addresses human readable format
def get_mac_addr(bytes_addr):
    bytes_str= map()