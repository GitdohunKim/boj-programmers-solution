from sys import stdin

n, c, r = map(int, stdin.readline().split())
n = pow(2, n)
count = 0
while r > 1 or c > 1:
  n //= 2
  if r >= n:
    if c >= n:
      r, c = r - n, c-n
      count += n*n*3
    else:
      r = r-n
      count += n*n
  else:
    if c >= n:
      c = c-n
      count += n*n*2

count += c*2 + r
print(count)