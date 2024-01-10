def solution(numLog):
    answer = []
    for i in range(len(numLog) - 1):
        answer.append(get_operation(numLog[i+1] - numLog[i]))
    return ''.join(answer)

def get_operation(diff):
    if diff == 1:
        return "w"
    elif diff == -1:
        return "s"
    elif diff == 10:
        return "d"
    elif diff == -10:
        return "a"
    else:
        return ""
