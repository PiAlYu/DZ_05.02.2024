from ipaddress import *

for i in range(255, -1, -1):
    flag = 1
    ip = "223.167." + str(i) + ".167"
    mask = "255.255.255.192"
    a = ip_network(f'{ip}/{mask}', 0)
    for x in a:
        h = f'{x:b}'[:16]
        h1 = f'{x:b}'[16:]
        if h.count('0') > h1.count('0'):
            flag = 0
    if flag == 1:
        print(i)
        break
