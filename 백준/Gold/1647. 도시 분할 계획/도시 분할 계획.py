import sys
from collections import namedtuple

Edge = namedtuple('Edge', ['house1', 'house2', 'cost'])

class DisjointSet:
    def __init__(self, size):
        self.parent = [x for x in range(size + 1)]
        self.rank = [0] * (size + 1)

    def find(self, house):
        if self.parent[house] != house:
            self.parent[house] = self.find(self.parent[house])
        return self.parent[house]

    def union(self, h1, h2):
        root1 = self.find(h1)
        root2 = self.find(h2)

        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

def minimum_spanning_tree(edges, num_of_houses):
    disjoint_set = DisjointSet(num_of_houses)
    num_of_edges = 0
    answer = 0

    for edge_info in sorted(edges, key=lambda e: e.cost):
        if disjoint_set.find(edge_info.house1) != disjoint_set.find(edge_info.house2):
            disjoint_set.union(edge_info.house1, edge_info.house2)
            num_of_edges += 1
            answer += edge_info.cost

        if num_of_edges == num_of_houses - 1:
            answer -= edge_info.cost
            break

    return answer

num_of_houses, num_of_roads = map(int, sys.stdin.readline().split())
edges = [Edge(*map(int, sys.stdin.readline().split())) for _ in range(num_of_roads)]

print(minimum_spanning_tree(edges, num_of_houses))
