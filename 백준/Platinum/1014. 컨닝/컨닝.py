from itertools import product
import sys

def count_ones(n):
    return bin(n).count('1')

def is_valid(i):
    while i:
        if i & 3 == 3:
            return False
        i >>= 1
    return True

valid = []
value = []
u_lens = [1]
u = 1

for i in range(1 << 10):
    if is_valid(i):
        valid.append(i)
        value.append(count_ones(i))
    if u == i:
        u_lens.append(len(valid))
        u <<= 1
        u += 1

valid = tuple(valid)
value = tuple(value)
u_lens = tuple(u_lens)

input = sys.stdin.readline
C = int(input())

while C:
    C -= 1
    N, M = map(int, input().split())
    u_len = u_lens[M]
    bitmask = [-1] * u_len
    bitmask[0] = 0

    for _ in range(N):
        nbitmask = [-1] * u_len
        lmask = 0

        for s in input().rstrip():
            lmask <<= 1
            lmask += (s == 'x')

        for i, numi in enumerate(bitmask):
            if numi == -1:
                continue
            for j, numj in enumerate(nbitmask):
                if lmask & valid[j] or valid[i] & (valid[j] << 1) or valid[i] & (valid[j] >> 1):
                    continue
                if numj < numi + value[j]:
                    nbitmask[j] = numi + value[j]

        bitmask = nbitmask

    print(max(bitmask))
