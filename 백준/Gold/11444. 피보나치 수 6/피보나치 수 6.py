import sys

def multiply(matrix1, matrix2):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            result[i][j] = (matrix1[i][0] * matrix2[0][j] + matrix1[i][1] * matrix2[1][j]) % 1000000007
    return result

def exponentiate(matrix, power):
    if power == 1:
        return matrix
    
    half_power = exponentiate(matrix, power // 2)
    squared = multiply(half_power, half_power)
    
    if power % 2 == 1:
        squared = multiply(squared, matrix)
    
    return squared

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    base_matrix = [[1, 1], [1, 0]]
    
    result = exponentiate(base_matrix, N)
    
    print(result[1][0] % 1000000007)
