import scapy.all as scapy

def scanner(ip):
    request = scapy.ARP(pdst=ip)
    #request.pdst = ip
    # a maneira acima é uma alternativa para o primeiro request
    # request.show()
    print(request.summary())
    scapy.ls(scapy.ARP()) # Lista os argumentos

    broadcast = scapy.Ether()
    broadcast.dst = "coloque o broadcast mac aqui" #broadcast mac
    broadcast.show()

    request_broadcast = broadcast/request
    request_broadcast.show()

    resp1,resp2 = scapy.srp(request_broadcast, timeout = 1)
    # os dois resp estão armazenados em forma de lista

    for el in resp1:
        print(el[1].psrc)
        print(el[1].hwsrc)
        print("------------------------------------------------")
        # você pode utilizar o resp2 no lugar do resp1 para ver algumas informações
        # a mais nesse for.

scanner("Coloque o ip aqui")

"""CÓDIGO FEITO PARA UTILIZAÇÕES DIDÁTICAS!!!!!!!!!!!"""