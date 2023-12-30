import sys

def DP(x):

    if x == 1:
        num[1] = 1
    elif x == 2:
        num[2] = 2
    elif x == 3:
        num[3] = 4
    else:
        num[x] = num[x-1] + num[x-2] + num[x-3]

num = {}

for i in range(1, 11):
    DP(i)

T = int(input())
for _ in range(T):
    n = int(input())
    print(num[n])
