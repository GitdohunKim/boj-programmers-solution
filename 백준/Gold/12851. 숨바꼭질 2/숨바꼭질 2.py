from collections import deque
import sys

def BFS(nodes, visited, K, output):
    newNodes = []
    count = 0
    output += 1

    for n in nodes:
        visited[n] = 1
        for mn in (n + 1, n - 1, 2 * n):
            if mn == K:
                count += 1
            elif 100001 > mn > -1 and visited[mn] == 0:
                newNodes.append(mn)

    if count != 0:
        print(output)
        print(count)
    else:
        BFS(newNodes, visited, K, output)

def main():
    global output
    sys.setrecursionlimit(10**7)
    N, K = map(int, sys.stdin.readline().split())
    visited = [0] * 100001
    visited[N] = 1
    output = 0

    if N == K:
        print(0)
        print(1)
    else:
        BFS([N], visited, K, output)

if __name__ == "__main__":
    main()
