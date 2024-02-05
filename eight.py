def find_multiplicative_inverse(det):
  inv = -1
  for i in range(26):
    inv = det * i
    if inv % 26 == 1:
      inv = i
      break
  return inv


def decrypt_hill(cipher, key):
  det = (key[0][0] * key[1][1] - key[1][0] * key[0][1])
  inv_det = find_multiplicative_inverse(det)
  key_inverse = key
  key_inverse[0][0], key_inverse[1][1] = key[1][1], key[0][0]
  key_inverse[0][1] *= -1
  key_inverse[1][0] *= -1
  for i in range(2):
    for j in range(2):
      key_inverse[i][j] *= inv_det
      key_inverse[i][j] %= 26

  A = "abcdefghijklmnopqrstuvwxyz"

  cipher = cipher.lower()

  cipher_n = [A.index(char) for char in cipher]

  pairs = [cipher_n[i:i+2] for i in range(0,len(cipher),2)]

  print(pairs)

  plain = []
  for pair in pairs:
    i = [(key_inverse[0][0] * pair[0] + key_inverse[0][1] * pair[1]) % 26,
           (key_inverse[1][0] * pair[0] + key_inverse[1][1] * pair[1]) % 26 
    ]
    plain += i
  
  print("".join(A[ind] for ind in plain))

decrypt_hill("fkmfio", [[2,3],[3,6]])