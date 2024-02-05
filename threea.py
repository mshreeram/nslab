# 3.a RSA Algorithm

def gcd(a, h):
  temp = 0
  while(1):
    temp = a % h
    if (temp == 0):
      return h
    a = h
    h = temp

p = 7
q = 11
e = 7
n = p * q
phi = (p - 1) * (q - 1)

while(e < phi):
  if(gcd(e, phi) == 1):
    break
  else:
    e = e + 1

print("e: ", e)

d = pow(e, -1, phi)

print("d: ", d)

def decrypt(cipher):
  msg = (cipher ** d) % n
  print(msg)

decrypt(37)