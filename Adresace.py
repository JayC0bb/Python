import ipaddress

 sit = input("Síť:")
IPadresa = ipaddress.IPv4Network(sit)
 print("Maska:", IPadresa.netmask)
 print("Network:", IPadresa.network_address)
 print("Broadcast:", IPadresa.broadcast_address)
adres = IPadresa.num_addresses
 print("Adresy:", adres)
 print("Hosti:", adres-2)
