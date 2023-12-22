def solution(n):
    count = 0
    value = 0
    s = 1
    while True:
        if s == n+1:
            break
        for i in range(s , n+1):
            value += i
            if value == n:
                count += 1
            elif value > n:
                value = 0
                break
        value = 0  
        s += 1

    return count