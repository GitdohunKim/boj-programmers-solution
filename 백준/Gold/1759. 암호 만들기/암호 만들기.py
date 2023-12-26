vowel = ['a', 'e', 'i', 'o', 'u']
l, c = map(int, input().split())
words = list(map(str, input().split()))
words.sort()
ans = []
visited = [0] * c

def is_vowel(ans): # 모음 포함 여부
    for i in range(len(vowel)):
        if vowel[i] in ans:
            return 1
    return 0

def is_two_cons(ans): # 자음 2개 포함 여부
    cnt = 0
    for i in range(len(ans)):
        if ans[i] not in vowel: # 모음이 아니면 cnt를 1 더한다 = 자음
            cnt += 1
    if cnt >= 2:
        return 1
    else:
        return 0

def dfs(iter):
    if len(ans) == l:
        if is_vowel(ans) and is_two_cons(ans): # 모음 1개 이상, 자음 2개 이상
            print(''.join(ans))
            return
    for i in range(iter, c):
        if not visited[i]:
            ans.append(words[i])
            visited[i] = 1
            dfs(i)
            visited[i] = 0
            ans.pop()
dfs(0)