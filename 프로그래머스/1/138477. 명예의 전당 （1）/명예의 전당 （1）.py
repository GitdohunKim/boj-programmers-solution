def solution(k, score):
    answer = []
    for i in range(len(score)):
        answer.append(min(sorted(score[0:i+1],reverse=True)[:k]))
    return answer