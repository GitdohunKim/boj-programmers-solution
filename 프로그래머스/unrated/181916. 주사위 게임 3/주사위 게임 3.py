def solution(a, b, c, d):
    if a==b==c==d:
        return 1111*a
    elif a==b==c:
        return (10*a+d)**2
    elif a==b==d:
        return (10*a+c)**2
    elif a==d==c:
        return (10*a+b)**2 
    elif d==b==c:
        return (10*b+a)**2
    elif a==b and c==d:
        return (a+c)*(a-c) if a>c else  (a+c)*(c-a)
    elif a==c and b==d:
        return (a+b)*(a-b) if a>b else  (a+b)*(b-a)
    elif a==d and c==b:
        return (a+c)*(a-c) if a>c else  (a+c)*(c-a)
    elif a==b:
        return c*d
    elif a==c:
        return b*d
    elif a==d:
        return c*b
    elif d==b:
        return a*c
    elif c==b:
        return a*d
    elif c==d:
        return a*b
    else:
        return min(a,b,c,d)