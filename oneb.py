# 1.b Dterminant and adjoint of a two by two (2 * 2) matrix

my_matrix = [[2, 3], [3, 6]]

# Determinant Calculation
def determinant_of_a_matrix(matrix):
  determinant = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]) 
  print("determinant: ", determinant % 26)

# Adjoint Calculation
def adjoint_of_a_matrix(matrix):
  adj = [[matrix[1][1] % 26, - matrix[1][0] % 26], [ - matrix[0][1] % 26, matrix[0][0] % 26]]
  print("Adj: ", adj)

determinant_of_a_matrix(my_matrix)
adjoint_of_a_matrix(my_matrix)