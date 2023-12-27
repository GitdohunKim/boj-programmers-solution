def solution():
    stdin = open(0, "rb")
    T = int(stdin.readline())
    for _ in range(T):
        K = int(stdin.readline())
        sizes = list(map(int, stdin.readline().split()))

        ans = 0
        cursor = 1
        q = [1_000_000_000, sizes[0]] + [0] * K

        def combine(end):
            nonlocal ans
            nonlocal cursor
            cost = q[end-1] + q[end]
            ans += cost

            for i in range(end, cursor):
                q[i] = q[i+1]
            
            i = end-2
            while q[i] < cost:
                q[i+1] = q[i]
                i -= 1
            q[i+1] = cost

            cursor -= 1
            while i > 0 and q[i-1] <= cost:
                d = cursor-i
                combine(i)
                i = cursor-d
        ### enddef combine

        for x in sizes[1:]:
            while q[cursor-1] <= x:
                combine(cursor)
            cursor += 1
            q[cursor] = x
        while cursor > 1:
            combine(cursor)
        print(ans)
### enddef solution

solution()