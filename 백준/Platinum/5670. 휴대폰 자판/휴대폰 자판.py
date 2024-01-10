from sys import stdin

input = stdin.readline

class Node:
    def __init__(self, alpha):
        self.alpha = alpha
        self.child = []
        self.is_word = False

def solve():
    global total
    while True:
        total = 0
        n, words = input_data()
        if n == -1:
            break

        trie = make_trie(words)
        for start in trie.child:
            simulate(start, 1)
        print('%.2f' % round(total / n, 2))

def simulate(now, count):
    global total
    if now.is_word:
        total += count
    if now.child:
        if not now.is_word and len(now.child) == 1:
            simulate(now.child[0], count)
        else:
            for nxt in now.child:
                simulate(nxt, count + 1)

def make_trie(words):
    trie = Node('-')
    now = trie
    for word in words:
        for alpha in word:
            now = search_child(now, alpha)
        now.is_word = True
        now = trie
    return trie

def search_child(now, target):
    for child in now.child:
        if child.alpha == target:
            return child
    node = Node(target)
    now.child.append(node)
    return node

def input_data():
    try:
        n = int(input())
        words = [input().strip() for _ in range(n)]
        return n, words
    except:
        return -1, []

solve()
