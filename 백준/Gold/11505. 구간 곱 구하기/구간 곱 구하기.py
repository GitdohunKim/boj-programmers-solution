import sys

def initialize_tree(left, right, idx, array, tree):
    if left == right:
        tree[idx] = array[left] % 1000000007
        return tree[idx] % 1000000007
    mid = (left + right) // 2
    tree[idx] = (initialize_tree(left, mid, 2 * idx, array, tree) * initialize_tree(mid + 1, right, 2 * idx + 1, array, tree)) % 1000000007
    return tree[idx]

def query_tree(left, right, idx, node_left, node_right, tree):
    if node_right < left or right < node_left:
        return 1
    if left <= node_left and node_right <= right:
        return tree[idx]
    mid = (node_left + node_right) // 2
    return (query_tree(left, right, 2 * idx, node_left, mid, tree) * query_tree(left, right, 2 * idx + 1, mid + 1, node_right, tree)) % 1000000007

def update_tree(index, new_value, node_idx, node_left, node_right, tree):
    if index < node_left or index > node_right:
        return tree[node_idx]
    if node_left == node_right:
        tree[node_idx] = new_value % 1000000007
        return tree[node_idx] % 1000000007
    mid = (node_left + node_right) // 2
    tree[node_idx] = (update_tree(index, new_value, 2 * node_idx, node_left, mid, tree) * update_tree(index, new_value, 2 * node_idx + 1, mid + 1, node_right, tree)) % 1000000007
    return tree[node_idx]

def find_product(left, right, tree):
    return query_tree(left, right, 1, 0, len(tree) // 4 - 1, tree)

def update_value(index, value, tree):
    return update_tree(index, value, 1, 0, len(tree) // 4 - 1, tree)

def main():
    input_func = sys.stdin.readline
    n, m, k = map(int, input_func().split())
    nums = [int(input_func()) for _ in range(n)]
    segment_tree = [0] * (4 * n)
    initialize_tree(0, n - 1, 1, nums, segment_tree)

    for _ in range(m + k):
        a, b, c = map(int, input_func().split())
        if a == 1:
            update_value(b - 1, c, segment_tree)
        else:
            print(find_product(b - 1, c - 1, segment_tree))

if __name__ == "__main__":
    main()
