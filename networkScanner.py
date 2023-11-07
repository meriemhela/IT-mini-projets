from scapy.all import ARP, Ether ,srp

t_ip = input("Enter the target IP like 192.168.0.1/24 :")
arp = ARP(pdst=t_ip) #ARP request packet is created
ether = Ether(dst="ff:ff:ff:ff:ff:ff") #Ethernet frame is created (broadcast address)
packet = ether/arp #combinés pour former un paquet (en-tete ethernet+ arp)
result = srp(packet, timeout=3, verbose =0)[0] #envoyer le paquet et recevoir des réponses
clients=[]

for sent, received in result:
    clients.append({'ip':received.psrc,'mac':received.hwsrc}) # Pour chaque réponse, l'adresse IP et l'adresse MAC sont extraites du paquet

print("available devices in the network:")
print("IP"+ " "*18+"mac")

for client in clients:
    print("{:16}   {}".format(client['ip'],client['mac']))

