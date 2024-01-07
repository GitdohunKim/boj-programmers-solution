import sys

def get_parent(num_plane):
    if parent_arr[num_plane] == num_plane:
        return num_plane
    parent_arr[num_plane] = get_parent(parent_arr[num_plane])
    return parent_arr[num_plane]

g = int(sys.stdin.readline().rstrip())
p = int(sys.stdin.readline().rstrip())

parent_arr = [i for i in range(g + 1)]
result = 0

for _ in range(p):
    num_plane = int(sys.stdin.readline().rstrip())
    parent_plane = get_parent(num_plane)
    
    if not parent_plane:
        break
    
    parent_arr[parent_plane] = parent_arr[parent_plane - 1]
    result += 1

print(result)
