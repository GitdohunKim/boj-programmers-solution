import sys
input = sys.stdin.readline

n, m = map(int, input().split())
text, num = {}, {}

for i in range(1, n+1):
  name = input().strip()
  text[name] = i
  num[i] = name

for _ in range(m):
  pocket = input().strip()
  if pocket in text.keys():
    print(text[pocket])
  else: print(num[int(pocket)])