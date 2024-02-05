from ipaddress import *

k = 0
ip = "171.128.0.0"
mask = "255.128.0.0"
a = ip_network(f'{ip}/{mask}', 0)
for x in a:
    h = f'{x:b}'[:16]
    h1 = f'{x:b}'[16:]
    if h.count('1') < h1.count('1'):
        k += 1
print(k)
