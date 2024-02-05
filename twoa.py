# 2.a Brute force approach for decryption

def ceasar_dec(cipher):
  cipher = cipher.upper()
  ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  for key in range((len(ALPHABET))):
    translated = ''
    for symbol in cipher:
      if symbol in cipher:
        ind = ALPHABET.find(symbol)
        ind = ind - key
        if ind < 0:
          ind += len(ALPHABET)
        translated += ALPHABET[ind]
      
    print(f'key #{key}: {translated}')

# ceasar_dec('RFIMZWFBFIFANXFPMFUFYSFR')
ceasar_dec('mrjsvqexmsrrxiglrspskc')