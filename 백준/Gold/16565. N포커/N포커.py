import math

def calculate_combinations(n, k):
    return math.comb(n, k)

def calculate_sum(n):
    s = 0
    for i in range(1, n // 4 + 1):
        s += (-1) ** (i + 1) * calculate_combinations(13, i) * calculate_combinations(52 - 4 * i, n - 4 * i)
    return s % 10007

def main():
    n = int(input())
    result = calculate_sum(n)
    print(result)

if __name__ == "__main__":
    main()
