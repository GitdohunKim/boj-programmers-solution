def solution(a, d, included):
    mod = [a]
    answer = []
    for i in range(len(included)):
        mod.append(mod[i] + d)
        if included[i]:
            answer.append(mod[i])
        else:
            continue
    return sum(answer)