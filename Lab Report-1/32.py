def multiply_matrices(mat1, mat2):
   
    if len(mat1[0]) != len(mat2):
        raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
if __name__ == "__main__":
    mat1 = [[1, 2, 3], [4, 5, 6]]
    mat2 = [[7, 8], [9, 10], [11, 12]]
    result = multiply_matrices(mat1, mat2)
    print("Matrix 1:")
    for row in mat1:
        print(row)
    print("\nMatrix 2:")
    for row in mat2:
        print(row)
    print("\nResult:")
    for row in result:
        print(row)