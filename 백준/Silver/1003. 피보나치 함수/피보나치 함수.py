import sys
def f(n, d):
    if n in d: return d[n]
    if 0<=n<=1: return 1
    else:
        sol=f(n-1, d)+f(n-2, d)
        d[n]=sol
        return sol
N=int(sys.stdin.readline().rstrip())
d={}
for i in range(N):
    M=int(sys.stdin.readline().rstrip())
    if M==0: print('1 0')
    elif M==1: print('0 1')
    else: print(f(M-2, d), f(M-1, d))