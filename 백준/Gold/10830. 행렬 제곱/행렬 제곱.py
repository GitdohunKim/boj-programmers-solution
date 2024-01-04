def matrix_multiplication(mat_A, mat_B):
    mat_C = [[0] * len(mat_B[0]) for _ in range(len(mat_A))]
    for i in range(len(mat_A)):
        for j in range(len(mat_B[0])):
            for k in range(len(mat_B)):
                mat_C[i][j] += mat_A[i][k] * mat_B[k][j]
            mat_C[i][j] %= 1000

    return mat_C

def matrix_power(mat, exp):
    if exp == 1:
        return [[element % 1000 for element in row] for row in mat]

    half_power = matrix_power(mat, exp // 2)
    result = matrix_multiplication(half_power, half_power)

    if exp % 2 == 0:
        return result
    else:
        return matrix_multiplication(result, mat)

def print_matrix(matrix):
    for row in matrix:
        print(*row)

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result_matrix = matrix_power(A, B)
print_matrix(result_matrix)
