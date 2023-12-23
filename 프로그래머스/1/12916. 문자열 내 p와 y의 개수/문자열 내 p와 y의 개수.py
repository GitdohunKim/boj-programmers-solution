def solution(s):
    answer = list(s.lower())
    return True if answer.count('p') == answer.count('y') else False