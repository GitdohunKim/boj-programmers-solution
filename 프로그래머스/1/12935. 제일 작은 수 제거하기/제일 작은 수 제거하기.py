def solution(arr):
    arr.pop(arr.index(min(arr)))
    if arr == []:
        return [-1]
    return arr