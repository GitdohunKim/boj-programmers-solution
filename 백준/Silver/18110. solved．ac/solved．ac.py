n, *a = map(int, open(0))

if not n:
    print(0)
    exit()
    
t = int(n * 3 / 20 + 0.5)
m = int(sum(sorted(a)[t:n - t]) / (n - t * 2) + 0.5) 
print(m)