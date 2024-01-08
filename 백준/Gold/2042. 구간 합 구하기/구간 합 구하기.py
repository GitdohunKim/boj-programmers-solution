import sys

def main():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    size = 1 << (len(bin(n)) - 2)
    size_times_2 = size * 2
    n_plus_1 = n + 1
    tree = [0] * size_times_2

    for i in range(size + 1, size + n_plus_1):
        tree[i] = int(input())

    for i in range(size - 1, 0, -1):
        tmp = i * 2
        tree[i] = tree[tmp] + tree[tmp + 1]

    stack = []

    for _ in range(m + k):
        a, b, c = map(int, input().split())

        if a == 1:
            b += size
            tree[b] = c
            b >>= 1

            while b:
                tmp = b * 2
                tree[b] = tree[tmp] + tree[tmp + 1]
                b >>= 1
        else:
            ans = 0
            stack.append((1, 0, size, b, c + 1))

            while stack:
                i, s, e, p, q = stack.pop()

                if s == p and e == q:
                    ans += tree[i]
                    continue

                k = (s + e) >> 1
                i *= 2

                if p < k:
                    stack.append((i, s, k, p, min(q, k)))

                if q > k:
                    stack.append((i + 1, k, e, max(p, k), q))

            print(ans)

main()
