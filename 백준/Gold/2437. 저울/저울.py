import sys

input = sys.stdin.readline

num_weight = int(input())
weights = list(map(int, input().split()))

weights.sort()

if weights[0] != 1:
    print(1)
else:
    max_measurable_weight = [0] * num_weight
    max_measurable_weight[0] = weights[0]
    for i in range(1, num_weight):
        max_measurable_weight[i] = max_measurable_weight[i - 1] + weights[i]

    for i in range(1, num_weight):
        if weights[i] > max_measurable_weight[i - 1] + 1:
            print(max_measurable_weight[i - 1] + 1)
            break
    else:
        print(max_measurable_weight[num_weight - 1] + 1)
