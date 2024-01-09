from sys import stdin

def main():
    input = stdin.readline
    n = int(input())
    a = [[40_001, -40_001] for _ in range(80_001)]
    domain = [40_001, -40_001]

    for _ in range(n):
        x, y = map(int, input().split())
        a[x][0] = min(a[x][0], y)
        a[x][1] = max(a[x][1], y)
        domain[0] = min(domain[0], x)
        domain[1] = max(domain[1], x)

    lower = [(domain[0], a[domain[0]][0], 0, -1)]
    upper = [(domain[0], a[domain[0]][1], 0, 1)]

    for i in range(domain[0] + 1, domain[1] + 1):
        if a[i][0] == 40_001:
            continue

        tmp1 = i - lower[-1][0]
        tmp2 = a[i][0] - lower[-1][1]
        while lower[-1][2] * tmp2 <= lower[-1][3] * tmp1:
            lower.pop()
            tmp1 = i - lower[-1][0]
            tmp2 = a[i][0] - lower[-1][1]
        lower.append((i, a[i][0], tmp1, tmp2))

        tmp1 = i - upper[-1][0]
        tmp2 = a[i][1] - upper[-1][1]
        while upper[-1][2] * tmp2 >= upper[-1][3] * tmp1:
            upper.pop()
            tmp1 = i - upper[-1][0]
            tmp2 = a[i][1] - upper[-1][1]
        upper.append((i, a[i][1], tmp1, tmp2))

    result = len(lower) + len(upper) - (a[domain[0]][0] == a[domain[0]][1]) - (a[domain[1]][0] == a[domain[1]][1])
    print(result)

main()
