"""
Program to perform Matric Multiplication 
"""

def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0]) if rows_a > 0 else 0
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0]) if rows_b > 0 else 0
    if cols_a != rows_b:
        print("Number of columns in Matrix A must be equal to number of rows in Matrix B")
        return
    result_matrix = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result_matrix

matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[7, 8], [9, 10], [11,12]]

result = multiply_matrices(matrix_a, matrix_b)
print("Resultant Matrix after multiplication:")
print(result)