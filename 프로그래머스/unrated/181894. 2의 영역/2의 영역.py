def solution(arr):
    a = arr.copy()
    a.reverse()
    for i in range(len(a)):
        if a[i] == 2:
            break
    for j in range(len(arr)):
        if arr[j] == 2:
            break
    answer = arr[j:len(a)-i]
    if not answer:
        return [-1]
    return answer