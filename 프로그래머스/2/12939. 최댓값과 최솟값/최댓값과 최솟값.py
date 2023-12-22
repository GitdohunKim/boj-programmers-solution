def solution(s):
    a= max(list(map(int,s.split())))
    b= min(list(map(int,s.split())))
    return f"{str(b)} {str(a)}"