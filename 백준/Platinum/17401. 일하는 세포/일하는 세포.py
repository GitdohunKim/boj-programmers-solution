import sys;t=sys.stdin.readline
k=int
def f():return map(k,t().split())
T,N,D=f()
y=[]
r=range
g=len
for _ in r(T):
    x=[[0 for j in r(N)] for i in r(N)]
    for i in r(k(t())):a,b,c=f();x[a-1][b-1]=c
    y.append(x)
def l(a,b):return [[sum([a[i][j]*b[j][k] for j in r(g(a[0]))])%(10**9+7) for k in r(g(b[0]))] for i in r(g(a))]
def u(a,n):
    if n==1:return a
    x=bin(n);b=list(a)
    for i in r(3,g(x)):
        b=l(b,b)
        if x[i]=='1':b=l(b,a)
    return b
if D//T:
    b=y[0]
    for i in r(1,T):b=l(b,y[i])
    a=u(b,D//T)
    for i in r(D%T):a=l(a,y[i])
else:
    a=y[0]
    for i in r(1,D):a=l(a,y[i])
for i in a:print(*i)