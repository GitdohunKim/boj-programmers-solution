import sys
input = sys.stdin.readline

n = int(input())
d = [list(map(str, input().split()))[1:] for _ in range(n)]
dic = {}

def trie(dic, arr):
    if len(arr) == 0:
        return 
    if arr[0] not in dic:
        dic[arr[0]] = {}
    trie(dic[arr[0]], arr[1:])

def dfs(i, dic):
    if not dic.keys():
        return
    for j in sorted(dic.keys()):
        print('--' * i + j)
        dfs(i + 1, dic[j])

for i in range(n):
    trie(dic, d[i])

dfs(0, dic)
