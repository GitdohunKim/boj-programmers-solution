def solution(numbers, n):
    answer = numbers[0]
    for i in range(1,n+1):
        if answer <= n:
            answer += numbers[i]
    return answer