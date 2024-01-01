from itertools import combinations

def solution(number):
    n = len(number)
    count = 0
    for combination in combinations(range(n), 3):
        if sum(number[i] for i in combination) == 0:
            count += 1
    return count