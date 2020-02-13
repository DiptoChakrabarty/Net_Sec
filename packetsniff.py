import socket
import struct
import textwrap

#Unpack etehrnet packet

def ether_frame(data):
    dest_mac,src_mac,proto=struct.unpack('! 6s 6s H',data[:14])
    print("***********")
    print(dest_mac,src_mac)
    return get_mac_addr(dest_mac),get_mac_addr(src_mac),socket.htons(proto),data[:20]
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
        raw_data,addr = conn.recvfrom(65535)
        #Obatin all data packets
        dest_mac,src_mac,eth_proto,data=ether_frame(raw_data)
        print(data)
        print("\nEthernet Frame : ")
        print("Destination: {},Source: {} , Protocol: {}".format(dest_mac,src_mac,eth_proto))
        # 8 for IPv4
        if eth_proto == 8:
            version,header_length,ttl,proto,src,target,new_data = unpack_packets(data[:20])
            print("Ipv4 Packets")
            print("Version",version)
            print("Header Length",header_length)
            print("TTl",ttl)
            print("Protocol",proto)
            print("Source",src)
            print("Target",target)

            # protocol 1 is for icmp data packets
            if eth_proto == 1:
                icmp_type, code ,checksum,data = icmp_packet(data)
                print("Icmp Packet")
                print("Icmp Packet type",icmp_packet)
                print("Code",code)
                print("CheckSum",checksum)
            # Tcp protocol has 6
            elif eth_proto == 6:
                src_port,dest_port,sequence,acknowledgement,flag_urg,flag_ack,flag_psh,flag_rst,flag_syn,flag_fin,data = tcp_packet(data)
                print("Tcp Packet")
                print(" Source and Destination ports : ",src_port,dest_port)
                print("Sequence and Acknowledgement",sequence,acknowledgement)
                print("Flags")
                print("URG : {} ACK : {} PSH : {} RST : {} SYN : {}  FIN : {}".format(flag_urg,flag_ack,flag_psh,flag_rst,flag_syn,flag_fin))
                print("Data Obtained")
                print(format_multi_line(data))
            # UDP 
            elif eth_proto == 17:
                src_port,dest_port,size,data = udp_segment(data)
                print("UDP")
                print("Source and Destination",src_port,dest_port)
                print("Size of Data",size)


#Unpack IPv4 packets
def unpack_packets(data):
    version_header_length=data[0]
    version=version_header_length >> 4
    print(version)
    print(data,len(data))
    header_length = (version_header_length & 15)*4
    print(header_length)
    if(len(data)>20):
        x=20
    else:
        x=-1
    ttl,proto,src,target = struct.unpack('! 8x B B 2x 4s 4s',data)
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

#Unpack UDP packets
def udp_unpack(data):
    src_port,dest_port,size=struct.unpack('! H  H 2x H',data[:8])
    return  src_port,dest_port,size,data[8:]

# Format multi line of data
def format_multi_line(prefix,string,size=80):
    size -= len(prefix)
    if isinstance(string,bytes):
        string = ''.join(r'\x{:02x}'.format(byte)  for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string,size)])



packet_capture()