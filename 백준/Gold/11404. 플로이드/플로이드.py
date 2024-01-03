import sys
input = sys.stdin.readline

inf = sys.maxsize

num_city = int(input())
num_bus = int(input())
graph = [[inf]*num_city for _ in range(num_city)]

for _ in range(num_bus):
    src, dst, cost = map(int, input().split())
    if cost < graph[src-1][dst-1]:
        graph[src-1][dst-1] = cost    

for v_mid in range(num_city):
    graph[v_mid][v_mid] = 0
    for v_src in range(num_city):
        for v_dst in range(num_city):
            new_dist = graph[v_src][v_mid]+graph[v_mid][v_dst]
            if new_dist < graph[v_src][v_dst]:
                graph[v_src][v_dst] = new_dist

int2str = lambda x: str(x) if x != inf else '0'
for row in graph:
    sys.stdout.write(' '.join(map(int2str, row))+'\n')