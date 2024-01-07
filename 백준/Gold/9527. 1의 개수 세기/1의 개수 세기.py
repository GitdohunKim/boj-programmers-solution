def count_set_bits(x):
    cnt = 0
    s = 0
    l = len(bin(x)) - 2

    for n in range(l - 1, -1, -1):
        if x & (1 << n):
            s += 1 + (0 if n == 0 else n * 2 ** (n - 1)) + cnt * 2 ** n
            cnt += 1

    return s

a, b = map(int, input().split())
result = count_set_bits(b) - count_set_bits(a - 1)
print(result)
