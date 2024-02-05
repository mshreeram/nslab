# 2.b Inverse of a matrix

def inverse_of_matrix(matrix):
  det = determinat_of_matrix(matrix)
  if det == 0:
    print("NO INVERSE FOR A SINGULAR MATRIX")
    return
  inv_det = 1 / det
  print("det: ", det)
  print("inv det: ", inv_det)
  inv = [
          [(matrix[1][1] * inv_det) % 26, (-matrix[1][0] * inv_det) % 26],
          [(-matrix[0][1] * inv_det) % 26, (matrix[0][0] * inv_det) % 26]
  ]
  print("inv: ", inv)

def determinat_of_matrix(matrix):
  return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26

inverse_of_matrix([[2, 3], [3, 6]])