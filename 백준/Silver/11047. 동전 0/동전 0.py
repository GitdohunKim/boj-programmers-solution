from sys import stdin

def calculate_min_coins(N, M, category):
    total_coins = 0

    while M > 0:
        for i in range(N-1, -1, -1):
            if category[i] <= M:
                num_coins = M // category[i]
                total_coins += num_coins
                M %= category[i]
                break

    return total_coins

if __name__ == "__main__":
    N, M = map(int, input().split())
    category = [int(stdin.readline()) for _ in range(N)]

    result = calculate_min_coins(N, M, category)
    print(result)


