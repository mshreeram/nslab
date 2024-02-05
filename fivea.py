# 5.a SubKey Gen DES

P_10_TABLE = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P_8_TABLE = [6, 3, 7, 4, 8, 5, 10, 9]

def generate_subkeys(key):
  initial_key = [key[i - 1] for i in P_10_TABLE]

  left_half = initial_key[:5]
  right_half = initial_key[5:]

  # left circular shift
  left_half = left_half[1:] + left_half[:1]
  right_half = right_half[1:] + right_half[:1]

  combined_key = left_half + right_half

  subkey1 = [combined_key[i - 1] for i in P_8_TABLE]

  # left circular shift by 2
  left_half = left_half[2:] + left_half[:2]
  right_half = right_half[2:] + right_half[:2]

  combined_key = left_half + right_half
  subkey2 = [combined_key[i - 1] for i in P_8_TABLE]

  print(subkey1, subkey2)

generate_subkeys([1, 0, 1, 0, 0, 0, 0, 0, 0, 0])
