# 3.a RSA Algorithm

# def gcd(a, h):
#   temp = 0
#   while(1):
#     temp = a % h
#     if (temp == 0):
#       return h
#     a = h
#     h = temp

p = 7
q = 11
e = 7
n = p * q
phi = (p - 1) * (q - 1)

# while(e < phi):
#   if(gcd(e, phi) == 1):
#     break
#   else:
#     e = e + 1

def encrypt(message):
  cipher = (message ** e) % n
  print(cipher)

encrypt(13)