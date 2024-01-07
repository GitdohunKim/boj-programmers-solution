import sys

def joyGo(N, num_list):
    def getPosition(num, lis_list):
        s, e = 0, len(lis_list) - 1
        while s <= e:
            m = (s + e) // 2
            if lis_list[m] == num:
                return m
            elif lis_list[m] < num:
                s = m + 1
            else:
                e = m - 1
        return s

    lis_list = [num_list[0]]
    dp = [(0, num_list[0])]

    for i in range(1, N):
        if num_list[i] > lis_list[-1]:
            lis_list.append(num_list[i])
            dp.append((len(lis_list) - 1, num_list[i]))
        else:
            position = getPosition(num_list[i], lis_list)
            lis_list[position] = num_list[i]
            dp.append((position, num_list[i]))

    result_list = [-1] * len(lis_list)
    last_position = len(lis_list) - 1
    for i in range(len(dp) - 1, -1, -1):
        if dp[i][0] == last_position:
            result_list[dp[i][0]] = dp[i][1]
            last_position -= 1

    return len(lis_list), result_list

N = int(input())
num_list = list(map(int, input().split()))

ans = joyGo(N, num_list)
print(ans[0])
print(*ans[1])
