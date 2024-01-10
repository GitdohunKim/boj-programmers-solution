def solution(arr, queries):
    answer = []
    for query in queries:
        i, j = query
        arr[i], arr[j] = arr[j], arr[i]
    answer = arr
    return answer