from bisect import bisect_left, bisect_right

def make_prefix_sum(target_arr):
    prefix = target_arr[:]
    
    for i in range(1, len(prefix)):
        prefix[i] += prefix[i-1]
        
    answer = prefix[:]
    for i in range(len(prefix)):
        for j in range(i + 1, len(prefix)):
            answer.append(prefix[j] - prefix[i])
        
    return sorted(answer)

T = int(input())
n = int(input())
array_a = list(map(int, input().split()))

m = int(input())
array_b = list(map(int, input().split()))

prefix_a = make_prefix_sum(array_a)
prefix_b = make_prefix_sum(array_b)

answer = 0
for x in prefix_a:
    target = T - x
    left = bisect_left(prefix_b, target)
    right = bisect_right(prefix_b, target)
    
    if left < len(prefix_b):
        answer += right - left

print(answer)
