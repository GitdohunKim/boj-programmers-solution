def solution(l, r):
    answer = []
    for num in range(l, r+1):
        if set(str(num)).issubset({'0', '5'}):
            answer.append(num)
    if not answer:
        return [-1]
    return answer