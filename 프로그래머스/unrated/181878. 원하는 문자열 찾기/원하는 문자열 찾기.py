def solution(myString, pat):
    a = myString.lower()
    b= pat.lower()
    if len(a)>= len(b):
        for  i in range(len(a)-len(b)+1):
            if a[i:i+len(b)] == b:
                return 1
    return 0