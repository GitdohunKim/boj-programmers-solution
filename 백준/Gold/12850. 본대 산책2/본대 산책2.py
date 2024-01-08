MOD = 1000000007

def mat_multiply(mat1, mat2):
    return [[sum(mat1[i][k] * mat2[k][j] % MOD for k in range(8)) % MOD for j in range(8)] for i in range(8)]

def mat_pow(mat, n):
    if n == 1:
        return mat

    half_power = mat_pow(mat, n // 2)
    result = mat_multiply(half_power, half_power)

    if n % 2 == 1:
        result = mat_multiply(result, mat)

    return result

def main():
    g = [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 0]
    ]

    n = int(input())
    result_matrix = mat_pow(g, n)
    print(result_matrix[0][0])

if __name__ == "__main__":
    main()
