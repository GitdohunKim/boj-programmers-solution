import sys
input = sys.stdin.readline

num = int(input())
memo = [0, 0]
for i in range(2, num+1):
  best = memo[i-1]+1
  if i % 2 == 0:
    best = min(memo[i//2]+1, best)
  if i % 3 == 0:
    best = min(memo[i//3]+1, best)
  memo.append(best)

print(memo[-1])