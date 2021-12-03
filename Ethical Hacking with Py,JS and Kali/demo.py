import scapy.all as scapy

def scanner(ip):
    request = scapy.ARP()
    #request.show()
    print(request.summary())

    broadcast = scapy.Ether()
    broadcast.dst = "ff:ff:ff:ff:ff:ff" #broadcast mac
    broadcast.show()

    request_broadcast = broadcast/request
    request_broadcast.show()

    resp1,resp2 = scapy.srp(request_broadcast, timeout = 1)