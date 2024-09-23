matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
def check_dimensions(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return False
    return True
if not check_dimensions(matrix1, matrix2):
    print("Matrices have different dimensions. Cannot add.")
    exit()
def add_matrices(matrix1, matrix2):
    result = [[matrix1[i][j] + matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result
result = add_matrices(matrix1, matrix2)
print("Result:")
for row in result:
    print(row)