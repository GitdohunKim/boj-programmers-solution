from sys import stdin
from heapq import heappop, heappush
from math import sqrt

def main():
    n = int(stdin.readline())
    stars = [tuple(map(float, stdin.readline().split())) for _ in range(n)]
    
    pq = [(0, stars[0][0], stars[0][1])]
    visit = set()
    result = 0
    
    while pq:
        d, x, y = heappop(pq)
        
        if (x, y) in visit:
            continue
        
        visit.add((x, y))
        result += d
        
        for a, b in stars:
            if (a, b) not in visit:
                heappush(pq, (sqrt((a-x)**2 + (b-y)**2), a, b))
    
    print(result)

if __name__ == "__main__":
    main()
