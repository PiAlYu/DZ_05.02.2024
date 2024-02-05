from ipaddress import *

for i in range(256):
  ip = "183.192." + str(i) + ".0"
  mask = "255.255.252.0"
  n = ip_network(f'{ip}/{mask}', 0)
  a, b = 0, 0
  for x in n:
    h = f'{x: b}'[16:]
    h1 = h.count('1')
    if h1 > 3:
      b += 1
    a += 1
  if a == b:
    print(a)
    break
