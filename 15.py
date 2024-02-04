from ipaddress import *

for i in range(33):
    network1 = ip_network(f'151.172.115.121/{i}', 0)
    network2 = ip_network(f'151.172.115.156/{i}', 0)
    if network1 != network2:
            print(i)
            break
