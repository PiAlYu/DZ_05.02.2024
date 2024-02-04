from ipaddress import *

k = 0
network = ip_network('192.168.32.160/255.255.255.240', 0)
for i in network:
    if f'{i:b}'.count('0') > 21:
        k += 1
print(k)
