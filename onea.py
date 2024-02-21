# 1.a Program to encrypt a text using Caesar Cipher

text = "Information Technology"
s = int(input("Enter a shift value: "))

def ceasar_enc(text, s):
  result = ""
# we cannot change the data given by the user.

for char in text:
    if char.isalpha():  
        if char.islower():
            result += chr((ord(char) - 97 + s) % 26 + 97)
        else:
            result += chr((ord(char) - 65 + s) % 26 + 65)
    else:
        result += char  
    return result
ceasar_enc(text, s)
