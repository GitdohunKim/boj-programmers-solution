def solution(n, costs):
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    costs.sort(key=lambda x: x[2]) 
    parent = [i for i in range(n)]  
    total_cost = 0  

    for edge in costs:
        island1, island2, cost = edge
        if find_parent(parent, island1) != find_parent(parent, island2):
            union_parent(parent, island1, island2) 
            total_cost += cost

    return total_cost
