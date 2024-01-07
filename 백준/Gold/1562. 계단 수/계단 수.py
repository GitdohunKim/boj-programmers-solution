import sys
sys.setrecursionlimit(10**6)

N = int(input())
DP = [[[-1 for _ in range(1<<10)] for _ in range(N)] for _ in range(10)]

def stair(number, length, visited):
    if length == N:
        return 1 if visited == (1<<10)-1 else 0

    if DP[number][length][visited] != -1:
        return DP[number][length][visited]

    count = 0
    for dn in (-1, 1):
        number_ = number + dn
        if 0 <= number_ < 10:
            count += stair(number_, length+1, visited | (1<<number_))

    DP[number][length][visited] = count
    return count

result = sum(stair(i, 1, 1<<i) for i in range(1, 10))
print(result % 1000000000)
