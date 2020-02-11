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
    bytes_str= map('{:02x}'.format,bytes_addr)
    # Format to two decimal places make chunks
    mac_addr = ":".join(bytes_str).upper()
    return mac_addr

def packet_capture():
    conn =socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(3))

    while True:
        raw_data,addr = conn.recvfrom(65536)
        #Obatin all data pcakets
        dest_mac,src_mac,eth_proto,data=ether_frame(raw_data)
        print("\nEthernet Frame : ")
        print("Destination: {},Source: {} , Protocol: {}".format(dest_mac,src_mac,eth_proto))

packet_capture()