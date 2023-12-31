def P(N) :
    if N <= 3 :
        return 1
    if N <= 5 :
        return 2
    
    dp = [0] * (N + 1)
    dp[1], dp[2], dp[3] = 1, 1, 1
    dp[4], dp[5] = 2, 2

    for i in range (6, N + 1) :
        dp[i] = dp[i - 1] + dp[i - 5]
    
    return dp

dp = P(100)

for _ in range (int(input())) :
    print(dp[int(input())])