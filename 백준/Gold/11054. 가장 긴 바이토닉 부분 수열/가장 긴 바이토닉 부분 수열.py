import sys

input = sys.stdin.readline
sequence_length = int(input())
sequence = list(map(int, input().split()))

increasing_lengths = [1] * sequence_length
decreasing_lengths = [1] * sequence_length

for i in range(sequence_length):
    for front in range(i):
        if sequence[i] > sequence[front]:
            increasing_lengths[i] = max(increasing_lengths[i], increasing_lengths[front] + 1)

for i in range(sequence_length - 1, -1, -1):
    for back in range(i + 1, sequence_length):
        if sequence[i] > sequence[back]:
            decreasing_lengths[i] = max(decreasing_lengths[i], decreasing_lengths[back] + 1)

result = max([increasing + decreasing for increasing, decreasing in zip(increasing_lengths, decreasing_lengths)]) - 1

print(result)
