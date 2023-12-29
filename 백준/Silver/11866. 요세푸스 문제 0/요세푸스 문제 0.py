from collections import deque
n,k=map(int,input().split())
dq=deque([*range(n)])
res = []
while dq:
    dq.rotate(-k+1)
    res.append(str(dq.popleft()+1))
print('<'+', '.join(res)+'>')