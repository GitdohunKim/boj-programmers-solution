import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(set(map(int, input().split())))

def combinations(start, selected):
    if len(selected) == m:
        print(' '.join(map(str, selected)))
        return

    for i in range(start, len(numbers)):
        combinations(i, selected + [numbers[i]])

combinations(0, [])
