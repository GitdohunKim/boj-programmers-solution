import sys
sys.setrecursionlimit(10 ** 6)
def solution(k, num, links):
    root_candidate = [True for i in range(len(num))]
    dp = [None for i in range(len(num))]
    max_sum = sum(num)
    for a, b in links:
        for i in (a,b):
            if i>=0:
                root_candidate[i] = False
    root = None
    for i in range(len(root_candidate)):
        if root_candidate[i]:
            root = i
            break

    def _travelsal(root, lower_bound):
        left, right = links[root]
        if dp[root] != None:
            return dp[root]
        dp_left, dp_right = [
            _travelsal(i, lower_bound) if i != -1 else [max_sum, 0] for i in [left, right]
        ]
        all_sum = num[root] + dp_left[0] + dp_right[0]
        two_sum = num[root] + min(dp_left[0], dp_right[0])
        if all_sum <= lower_bound:
            dp[root] = all_sum, dp_left[1] + dp_right[1] - 1
        elif two_sum <= lower_bound:
            dp[root] = two_sum, dp_left[1] + dp_right[1]
        else:
            dp[root] = num[root], dp_left[1] + dp_right[1] + 1
        return dp[root]

    left, right = max(num), max_sum
    while left < right:
        dp = [None for _ in range(len(num))]
        mid = (left + right) >> 1
        result = _travelsal(root, mid)
        if result[1] <= k:
            right = mid
        else:
            left = mid + 1
    print(left)
    return left