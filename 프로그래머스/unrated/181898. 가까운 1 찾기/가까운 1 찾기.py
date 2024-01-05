def solution(arr, idx):
    min_index = -1
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            min_index = i
            break
    return min_index