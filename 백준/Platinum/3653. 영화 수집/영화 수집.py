import sys
input = sys.stdin.readline

t = int(input())

def init_tree():
    for i in range(1, n+m+1):
        if i <= n:
            fw_tree[i] = i & -i
        else:
            fw_tree[i] = max(0, n - (i - (i & -i)))
            
def update_tree(cur_idx, next_idx):
    temp = cur_idx
    result = 0
    while temp > 0:
        result += fw_tree[temp]
        temp -= temp & -temp
    while cur_idx <= n+m:
        fw_tree[cur_idx] -= 1
        cur_idx += cur_idx & -cur_idx
    while next_idx <= n+m:
        fw_tree[next_idx] += 1
        next_idx += next_idx & -next_idx
    return n - result
    
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    fw_tree = [0]*(n+m+1)
    index_map = [n-i+1 for i in range(n+1)]
    init_tree()
    for i, e in enumerate(map(int, input().rstrip().split())):
        idx = index_map[e]
        if idx == n+i+1:
            print(0, end=' ')
        else:
            print(update_tree(idx, n+i+1), end=' ')
            index_map[e] = n+i+1
    print()