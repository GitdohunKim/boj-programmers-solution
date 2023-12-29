def fac(x):
    res = 1
    for i in range(1,x+1):
        res *= i
    return res

n = int(input())
s = str(fac(n))

count = 0
for i in range(1, len(s)+1):
    if s[-i] == '0':
        count += 1
    else:
        break
print(count)