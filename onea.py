# 1.a Program to encrypt a text using Caesar Cipher

text = "Information Technology"
s = int(input("Enter a shift value: "))

def ceasar_enc(text, s):
  result = ""
  text = text.lower()
  for char in text:
    result += chr((ord(char) + s - 97) % 26 + 97)
  print(result)

ceasar_enc(text, s)