def solution(ineq, eq, n, m):
    if eq == "=":
        if ineq == "<":
            answer = int(n <= m)
        elif ineq == ">":
            answer = int(n >= m)
        else:
            answer = 0
    elif eq == "!":
        if ineq == "<":
            answer = int(n < m)
        elif ineq == ">":
            answer = int(n > m)
        else:
            answer = 0
    else:
        answer = 0

    return answer