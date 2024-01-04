import sys
input = sys.stdin.readline

MOD = int(1e9) + 7

def main():
    total_sum = 0

    for _ in range(int(input())):
        N, S = map(int, input().split())
        reciprocal_N = pow(N, -1, MOD)
        total_sum = (total_sum + S * reciprocal_N) % MOD

    print(total_sum)

if __name__ == "__main__":
    main()
