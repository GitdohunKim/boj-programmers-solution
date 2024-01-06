import sys

def is_palindrome(numbers, start, end, dp):
    return numbers[start] == numbers[end] and dp[start + 1][end - 1]

def build_palindrome_table(numbers):
    n = len(numbers)
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    for j in range(n - 1):
        if numbers[j] == numbers[j + 1]:
            dp[j][j + 1] = True

    for length in range(3, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            dp[start][end] = is_palindrome(numbers, start, end, dp)

    return dp

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    dp = build_palindrome_table(numbers)

    for _ in range(M):
        S, E = map(int, sys.stdin.readline().split())
        print(int(dp[S - 1][E - 1]))
