def solution(names):
    groups = [names[i:i+5] for i in range(0, len(names), 5)]
    return [group[0] for group in groups]