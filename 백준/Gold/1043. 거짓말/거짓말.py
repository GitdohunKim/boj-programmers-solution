import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())  
K, *T = map(int, input().split()) 
meet_graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
know_people = [0] * (N + 1)
party = []
q = deque()


def bfs():
    visited = [False] * (N + 1)
    while q:
        cur = q.popleft()
        visited[cur] = True
        know_people[cur] = 1 

        for i in range(1, N + 1):
            if meet_graph[cur][i] == 1 and not visited[i]:
                know_people[i] = 1
                q.append(i) 


result = 0

for i in range(K):
    q.append(T[i])  

for i in range(M):  
    num, *temp = map(int, input().split()) 
    party.append(temp)

    for j in range(num): 
        for k in range(num):
            if j != k:
                meet_graph[party[i][j]][party[i][k]] = 1 

bfs()

for i in range(M):
    for j in range(len(party[i])):
        if know_people[party[i][j]]:  
            break
    else:  
        result += 1
print(result)
