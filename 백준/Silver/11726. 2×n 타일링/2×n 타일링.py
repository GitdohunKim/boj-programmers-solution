import sys
input = sys.stdin.readline
from math import comb

def total_ways(n):
    ways = 0
    for x in range(n // 2 + 1):
        ways += comb(n - x, x)
    return ways % 10007

n = int(input())
print(total_ways(n))