def encrypt_hill(text, key):
  A = "abcdefghijklmnopqrstuvwxyz"
  text = text.lower()
  plain_text = [A.index(char) for char in text]

  # break the plain text into pairs
  pairs = [plain_text[i:i+2] for i in range(0, len(plain_text), 2)]

  cipher = []
  for pair in pairs:
    i = [(key[0][0] * pair[0] + key[0][1] * pair[1]) % 26,
         (key[1][0] * pair[0] + key[1][1] * pair[1]) % 26]
    cipher += i
  
  print(cipher)
  cipher_text = "".join(A[num] for num in cipher)
  print(cipher_text)

encrypt_hill("attack", [[2,3],[3,6]])