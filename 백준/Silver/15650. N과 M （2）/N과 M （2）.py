def back(start, s):
    if len(s) == M:                   
        print(' '.join(map(str, s)))

    for i in range(start, N+1):
        if i not in s:              
            s.append(i)            
            back(i+1, s)
            s.pop()

N, M = map(int, input().split())
s = []
back(1, s)
