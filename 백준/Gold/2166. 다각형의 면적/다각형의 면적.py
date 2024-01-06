import sys
import math
input = sys.stdin.readline

def solution():
  ans = 0
  for i in range(1, n+1):
    ans += vertex[i-1][0] * vertex[i][1] - vertex[i][0] * vertex[i-1][1]

  return 0.5 * round(abs(ans), 1)

n = int(input())
vertex = []
for _ in range(n):
  vertex.append(list(map(int, input().split())))
vertex.append(vertex[0])
print(solution())
