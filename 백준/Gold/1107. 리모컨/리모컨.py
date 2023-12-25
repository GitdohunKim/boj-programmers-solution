N = int(input())
M = int(input())

brokens = []
if M:
    brokens = input().split()


def check(n):
    strN = str(n)

    for s in strN:
        if s in brokens:
            return False
    return True


res = abs(100-N)

for i in range(1000000):
    if check(i):
        res = min(res, len(str(i))+abs(i-N))

print(res)