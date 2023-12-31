import sys

input = sys.stdin.readline

def tiling(n) :
    dp = [0] * (n+1)
    dp[1] = 1
    if n >= 2 :
        dp[2] = 3
    if n >= 3 :
        dp[3] = 5
    
    for i in range(4, n+1) :
        if i % 2 == 0 :
            dp[i] = dp[i-1]*2 + 1
        else :
            dp[i] = dp[i-1]*2 - 1
    
    return dp[n]

n = int(input())

result = tiling(n) % 10007

print(result)