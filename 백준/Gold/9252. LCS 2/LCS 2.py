import sys

def longest_common_subsequence(str1, str2):
    len_str1, len_str2 = len(str1), len(str2)

    # dp 배열 초기화
    dp = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]

    # 최장 공통 부분 수열 길이 계산
    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 최장 공통 부분 수열 출력
    length = dp[-1][-1]
    if length == 0:
        return 0, ""
    
    # 수열 역추적
    i, j = len_str1, len_str2
    lcs = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return length, ''.join(reversed(lcs))

if __name__ == "__main__":
    str1 = sys.stdin.readline().rstrip()
    str2 = sys.stdin.readline().rstrip()

    lcs_length, lcs_sequence = longest_common_subsequence(str1, str2)

    print(lcs_length)
    if lcs_length > 0:
        print(lcs_sequence)
