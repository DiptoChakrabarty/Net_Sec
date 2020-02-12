import socket
import struct
import textwrap

#Unpack etehrnet packet

def ether_frame(data):
    dest_mac,src_mac,proto=struct.unpack('! 6s 6s H',data[:14])
    print("***********")
    print(dest_mac,src_mac)
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

#Unpack IPv4 packets
def unpack_packets(data):
    version_header_length=data[0]
    version=version_header_length >> 4
    print(version)
    header_length = (version_header_length & 15)*4
    print(header_length)
    ttl,proto,src,target = struct.unpack('! 8x B B 2x 4s 4s',data[:20])
    print("///////////////")
    print(ttl,proto,src,target)
    return version,header_length,ttl,proto,ipv4(src),ipv4(target),data[header_length:]

#Returns formatted ipv4 addresses

def ipv4(addr):
    return '.'.join(map(str,addr))

#Unpack ICMP packets
def icmp_packet(data):
    icmp,code,checksum = struct.unpack('! B B H',data[:4])
    return icmp_type,code,checksum,data[4:]

#Unpack TCP packets
def tcp_packet(data):
    src_port,dest_port,sequence,acknowledgement,offset_reserved_flag = struct.unpack('! H H  L L H',data[:14])
    offset=(offset_reserved_flag >> 12)*4
    #Getting the tcp flags
    flag_urg =(offset_reserved_flag & 32) >> 5
    flag_ack =(offset_reserved_flag & 16) >> 5
    flag_psh =(offset_reserved_flag & 8) >> 5
    flag_rst =(offset_reserved_flag & 4) >> 5
    flag_syn =(offset_reserved_flag & 2) >> 5
    flag_fin =(offset_reserved_flag & 1) 
    return src_port,dest_port,sequence,acknowledgement,flag_urg,flag_ack,flag_psh,flag_rst,flag_syn,flag_fin,data[offset:]




packet_capture()