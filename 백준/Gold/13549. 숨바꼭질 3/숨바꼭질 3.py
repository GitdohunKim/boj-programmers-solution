import sys
from collections import deque

def bfs(start, goal):
    graph = [0] * 100001
    queue = deque()
    queue.append((start, 0))

    while queue:
        x, t = queue.popleft()

        if x == goal:
            return t

        dx = [x * 2, x - 1, x + 1]

        for i in dx:
            if 0 <= i <= 100000 and graph[i] == 0:
                if i == x * 2:
                    queue.append((i, t))
                else:
                    queue.append((i, t + 1))
                graph[i] = 1

if __name__ == "__main__":
    input_func = sys.stdin.readline
    start, goal = map(int, input_func().split())
    result = bfs(start, goal)
    print(result)
