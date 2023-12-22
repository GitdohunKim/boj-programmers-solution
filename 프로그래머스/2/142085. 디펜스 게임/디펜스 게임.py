import heapq

def solution(n, k, enemy):
    h = []
    for i, e in enumerate(enemy):
        heapq.heappush(h, e)
        if len(h) > k:
            n -= heapq.heappop(h)
        if n < 0:
            return i

    return len(enemy)