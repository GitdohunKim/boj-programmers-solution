import sys

def read():
    return sys.stdin.readline().rstrip()

def min_cost_to_reach_target(a, n, power):
    INF = 987654321
    d = [[[INF for _ in range(5)] for __ in range(5)] for ___ in range(n)]

    d[0][a[0]][0] = 2
    d[0][0][a[0]] = 2

    for i in range(1, n):
        target = a[i]

        for l in range(5):
            for r in range(5):
                move_right_power = power[r][target]
                d[i][l][target] = min(d[i][l][target], d[i-1][l][r] + move_right_power)

                move_left_power = power[l][target]
                d[i][target][r] = min(d[i][target][r], d[i-1][l][r] + move_left_power)

    answer = INF
    for row in d[n-1]:
        answer = min(answer, min(row))
    return answer

if __name__ == "__main__":
    a = list(map(int, read().split()))
    a.pop()
    n = len(a)

    power = [[987654321 for _ in range(5)] for __ in range(5)]
    for i in range(5):
        for j in range(1, 5):
            if i == 0:
                power[i][j] = 2
                continue
            if i == j:
                power[i][j] = 1
                continue
            if (i + 2) % 4 == j:
                power[i][j] = 4
                continue
            power[i][j] = 3
    power[2][4] = 4

    result = min_cost_to_reach_target(a, n, power)
    print(result)
