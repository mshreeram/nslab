# 1.a Program to encrypt a text using Caesar Cipher

text = "Information Technology"
s = int(input("Enter a shift value: "))

def ceasar_enc(text, s):
  result = ""
  #text = text.lower()
  #we cannot change the data given by user to upper case or lower case
  for char in text:
    if(char.islower()):
      result += chr((ord(char) + s - 97) % 26 + 97)
    else:
      result += chr((ord(char) + s - 65) % 26 + 65)
  print(result)

ceasar_enc(text, s)
