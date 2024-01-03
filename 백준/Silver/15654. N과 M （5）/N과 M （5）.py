def generate_combinations(arr, m):
    def dfs(idx, current_list):
        if idx == m:
            result.append(current_list[:])
            return

        for i in arr:
            if not visited[i]:
                visited[i] = 1
                dfs(idx + 1, current_list + [i])
                visited[i] = 0

    result = []
    dfs(0, [])
    return result

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split(' '))))
visited = [0] * (arr[-1] + 1)

answer = generate_combinations(arr, m)

for combination in answer:
    print(*combination)
