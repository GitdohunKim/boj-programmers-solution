def solution(d, budget):
    result = 0
    count = 0
    for i in range(len(d)):
        result += sorted(d)[i]
        if result <= budget:
            count += 1
    return count