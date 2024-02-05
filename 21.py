from ipaddress import *

for i in range(16, 25):
    flag = 1
    ip = "246.51.128.202"
    a = ip_network(f'{ip}/{i}', 0)
    for x in a:
        h = f'{x:b}'[:16]
        h1 = f'{x:b}'[16:]
        if h.count('0') > h1.count('0'):
            flag = 0
    if flag == 1:
        print(int('1' * (i - 16) + '0' * (24 - i), 2))
        break
