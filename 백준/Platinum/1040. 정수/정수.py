def num_kind(N):
    return len(set(str(N)))

def num_list(N):
    unused = [i for i in range(10) if str(i) not in str(N)]
    used = [i for i in range(10) if str(i) in str(N)]
    return unused, used

def solve(N, K):
    N_str = str(N)

    if num_kind(N_str) == K:
        print(N_str)
        return

    for prefix_i in range(len(N_str) - 1, -1, -1):
        prefix_last = int(N_str[prefix_i]) + 1

        for prefix_last in range(int(N_str[prefix_i]) + 1, 10):
            prefix = N_str[:prefix_i] + str(prefix_last)

            left_num = K - num_kind(prefix)
            left_len = len(N_str) - prefix_i - 1

            if 0 <= left_num <= left_len:
                unused, used = num_list(prefix)

                if left_num == 0:
                    print(prefix + str(used[0]) * left_len)
                    return
                print(prefix + '0' * (left_len - left_num) + ''.join(map(str, unused[:left_num])))
                return

    N = max(K, len(N_str) + 1)
    print("1" + "0" * (N - K + 1) + "23456789"[:K - 2])

N, K = map(int, input().split())
solve(N, K)
