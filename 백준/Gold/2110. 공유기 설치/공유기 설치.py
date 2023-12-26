import sys

def F(L,l,r):
  while l<=r:
    m,n,c=(l+r)//2,L[0],1
    for i in range(1,len(L)):
      if L[i]>=n+m:c,n=c+1,L[i]
    if c<C:r=m-1
    else:global R;l,R=m+1,m

I=sys.stdin.readline

N,C=map(int,I().split())
L=sorted([int(I()) for _ in range(N)])

R=0
F(L,1,L[-1]-L[0])
print(R)