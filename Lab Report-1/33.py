rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(int(input(f"Enter element [{i+1}][{j+1}]: ")))
    matrix.append(row)
print("Original Matrix:")
for row in matrix:
    print(row)
transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(columns)]
print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)