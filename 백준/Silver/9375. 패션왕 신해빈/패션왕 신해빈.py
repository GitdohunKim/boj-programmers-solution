import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    d = dict()

    for _ in range(N):
        _, category = sys.stdin.readline().strip().split()

        if category in d:
            d[category] += 1
        else:
            d[category] = 1

    result = 1
    for val in d.values():
        result *= val + 1

    print(result - 1)
