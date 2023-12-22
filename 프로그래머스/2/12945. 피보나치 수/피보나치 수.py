import sys
sys.setrecursionlimit(10 ** 6)
def solution(n):
    if n<=1:
        return n
    else:
        a = [0,1,1]
        for i in range(2,n):
            a.append(a[i-1]+a[i])
        return a[n]%1234567