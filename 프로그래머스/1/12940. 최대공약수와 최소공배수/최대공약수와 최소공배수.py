def solution(n, m):
    a = 1
    for i in range(max(n,m),1,-1):
        if n%i == 0 and m%i ==0:
            a = i
            break
    b= m*n//a
    answer = [a,b]
    return answer