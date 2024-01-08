import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def build_preorder(inorder_start, inorder_end, postorder_start, postorder_end):
    if inorder_end < inorder_start or postorder_end < postorder_start:
        return

    root = postorder[postorder_end]
    print(root, end=' ')

    left_nodes = indexes[root] - inorder_start
    right_nodes = inorder_end - indexes[root]

    build_preorder(inorder_start, inorder_start + left_nodes - 1, postorder_start, postorder_start + left_nodes - 1)
    build_preorder(inorder_end - right_nodes + 1, inorder_end, postorder_end - right_nodes, postorder_end - 1)

if __name__ == "__main__":
    n = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))
    preorder = []

    indexes = [0] * (n + 1)
    for i in range(n):
        indexes[inorder[i]] = i

    build_preorder(0, n - 1, 0, n - 1)
