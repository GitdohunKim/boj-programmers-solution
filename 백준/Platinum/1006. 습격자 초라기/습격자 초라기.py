tc = int(input())

def func(start,end,isokay):
    for i in range(start,end):
        if li[1][i-1] + li[1][i] <= w:
            v = 1
        else:
            v = 2
        dp[i][0] = min(dp[i-1][1]+v,dp[i-1][2]+1)
        if li[0][i-1] + li[0][i] <= w:
            v = 1
        else:
            v = 2
        dp[i][1] = min(dp[i-1][0]+v,dp[i-1][2]+1)
        if li[0][i] + li[1][i] <= w:
            v = 1
        else:
            v = 2
        if (isokay or i>2) and li[0][i-1] + li[0][i] <= w and li[1][i-1] + li[1][i] <= w:
            dp[i][2] = min(dp[i-1][2]+v,dp[i][0]+1,dp[i][1]+1,dp[i-2][2]+2)
        else:
            dp[i][2] = min(dp[i-1][2]+v,dp[i][0]+1,dp[i][1]+1)

for _ in range(tc):
    n , w = map(int,input().split())
    li = [[0],[0]]
    for i in range(2):
        li[i].extend(map(int,input().split()))
        li[i][0] = li[i][-1]
    dp = [[0,0,0] for _ in range(n+1)]
    if n > 1:
        dp[1][0] , dp[1][1] = 1 , 1
        if li[0][1] + li[1][1] <= w:
            dp[1][2] = 1
        else:
            dp[1][2] = 2
        func(2,n+1,True)
        mindp = dp[n][2]
        if li[0][0]+li[0][1] <= w:
            dp = [[0,0,0] for _ in range(n+1)]
            dp[1] = [1 , 1 , 2]
            dp[2][1] = 3
            if li[1][1]+li[1][2] <= w:
                dp[2][0] = 2
            else:
                dp[2][0] = 3
            if li[0][2]+li[1][2] <= w:
                dp[2][2] = 3
            else:
                dp[2][2] = dp[2][0] + 1
            func(3,n,False)
            if li[1][n-1] + li[1][n] <= w:
                v = 1
            else:
                v = 2
            dp[n][0] = min(dp[n-1][1]+v,dp[n-1][2]+1)
            mindp = min(mindp,dp[n][0])
        if li[1][0]+li[1][1] <= w:
            dp = [[0,0,0] for _ in range(n+1)]
            dp[1] = [1 , 1 , 2]
            dp[2][0] = 3
            if li[0][1]+li[0][2] <= w:
                dp[2][1] = 2
            else:
                dp[2][1] = 3
            if li[0][2]+li[1][2] <= w:
                dp[2][2] = 3
            else:
                dp[2][2] = dp[2][1] + 1
            func(3,n,False)
            if li[0][n-1] + li[0][n] <= w:
                v = 1
            else:
                v = 2
            dp[n][1] = min(dp[n-1][0]+v,dp[n-1][2]+1)
            mindp = min(mindp,dp[n][1])
        if li[0][0]+li[0][1] <= w and li[1][0]+li[1][1] <= w:
            dp = [[0,0,0] for _ in range(n+1)]
            dp[1] = [1 , 1 , 2]
            dp[2][1] = 3
            dp[2][0] = 3
            if li[0][2]+li[1][2] <= w:
                dp[2][2] = 3
            else:
                dp[2][2] = 4
            func(3,n,False)
            mindp = min(mindp,dp[n-1][2])
        print(mindp)
    else:
        if li[0][1] + li[1][1] <= w:
            print(1)
        else:
            print(2)
