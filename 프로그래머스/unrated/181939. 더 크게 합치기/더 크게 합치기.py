def solution(a, b):
    c=str(a)
    d=str(b)
    return int(''.join(c+d)) if int(''.join(c+d)) > int(''.join(d+c)) else int(''.join(d+c))