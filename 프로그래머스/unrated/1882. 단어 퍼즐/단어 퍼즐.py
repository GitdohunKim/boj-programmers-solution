import sys

def solution(strs, t):
    strs_set = set(strs)
    n = len(t)
    dp = [sys.maxsize] * (n + 1)
    dp[0] = 0

    for i in range(n):
        s = i

        for j in range(1, 6):
            e = s + j
            if e > n:
                break

            substring = t[s:e]
            if substring in strs_set:
                dp[e] = min(dp[s] + 1, dp[e])

    return -1 if dp[-1] == sys.maxsize else dp[-1]