def solution(arr, intervals):
    answer = []
    a, b = intervals
    c, d = a
    e, f = b
    answer = arr[c:d+1]+arr[e:f+1]
    return answer