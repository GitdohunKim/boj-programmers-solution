def solution(arr, queries):
    for query in queries:
        start = query[0]
        end = query[1]
        for i in range(start, end+1):
            arr[i] += 1
    return arr