def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) < 1:
        answer.append(-1)
    return sorted(answer)