def palindrome_partition(s):
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for index in range(n):
        dp[index + 1] = dp[index] + 1
        for left in range(index):
            if s[left:index + 1] == s[left:index + 1][::-1]:
                dp[index + 1] = min(dp[index + 1], dp[left] + 1)

    return dp[-1]

if __name__ == "__main__":
    S = input().strip()
    result = palindrome_partition(S)
    print(result)
