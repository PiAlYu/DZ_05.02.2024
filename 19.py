from ipaddress import *

k = 0
for i in range(256):
    flag = 1
    ip = "207.0." + str(i) + ".167"
    mask = "255.255.255.192"
    a = ip_network(f'{ip}/{mask}', 0)
    for x in a:
        h = f'{x:b}'[:16]
        h1 = f'{x:b}'[16:]
        if h.count('0') <= h1.count('0'):
            flag = 0
    if flag == 1:
        k += 1
print(k)
