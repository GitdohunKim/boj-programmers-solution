import sys
q=[]
for _ in range(int(sys.stdin.readline())):
    e=sys.stdin.readline().rstrip().split()
    if e[0]=='push':
        q.append(e[1])
    elif e[0]=='pop':
        if not q:
            print(-1)
        else:
            print(q[0])
            q.remove(q[0])
    elif e[0]=='size':
        print(len(q))
    elif e[0]=='empty':
        if not q:
            print(1)
        else:
            print(0)
    elif e[0]=='front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif e[0]=='back':
        if not q:
            print(-1)
        else:
            print(q[-1])