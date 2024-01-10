def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        if e == len(arr):
            temp = [x for x in arr[s:]]
        else:
            temp = [x for x in arr[s:e+1]]
        condi = sorted([x for x in temp if x > k])
        if len(condi) == 0:
            answer.append(-1)
        else:
            answer.append(condi[0])
    return answer