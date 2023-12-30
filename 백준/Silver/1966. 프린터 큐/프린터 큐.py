for _ in range(int(input())):
    n, k = map(int,input().split())
    queue = list(enumerate(map(int, input().split())))
    ans = 0
    while queue:
        mx = max(tup[1] for tup in queue)
        idx, now = queue.pop(0)
        if now == mx:
            ans += 1
            if k == idx: break
        else: queue.append((idx, now))

    print(ans)