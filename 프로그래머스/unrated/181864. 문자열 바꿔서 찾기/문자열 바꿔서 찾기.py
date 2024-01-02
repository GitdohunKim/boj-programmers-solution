def solution(myString, pat):
    answer = 0
    pat= pat.replace('A', 'C').replace('B', 'A').replace('C', 'B')
    for i in range(len(myString) - len(pat) + 1):
        if myString[i:i+len(pat)] == pat:
            answer = 1
    return answer