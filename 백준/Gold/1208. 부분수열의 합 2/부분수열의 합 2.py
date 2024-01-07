import sys
from collections import Counter

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def get_subarray_sums(subarray):
    tmp_sums = [0]
    for num in subarray:
        tmp = [num + existing_sum for existing_sum in tmp_sums]
        tmp_sums.extend(tmp)
    return tmp_sums

def main():
    mid = N // 2

    left_subarray_sums = get_subarray_sums(arr[:mid])
    right_subarray_sums = Counter(get_subarray_sums(arr[mid:]))

    count = 0
    if S == 0: 
        count = -1 

    for left_sum in left_subarray_sums:
        right_sum = S - left_sum
        if right_sum in right_subarray_sums:
            count += right_subarray_sums[right_sum]
    
    print(count)

if __name__ == "__main__":
    main()
