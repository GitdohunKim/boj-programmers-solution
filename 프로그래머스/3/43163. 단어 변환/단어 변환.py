from collections import defaultdict

def count_different_chars(word1, word2):
    diff_count = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count += 1

    return diff_count

def solution(begin, target, words):
    answer = 0

    g = defaultdict(list)

    for i in words + [begin]:
        for y in words:
            if i == y:
                continue
            if count_different_chars(i, y) == 1:
                g[i].append(y)

    def dfs(word, trace):
        if word == target:
            return len(trace)

        if word in trace:
            return 0

        results = []
        for w in g[word]:
            r = dfs(w, trace + [word])
            if r != 0:
                results.append(r)
        return min(results) if results else 0

    r = dfs(begin, [])
    return r
