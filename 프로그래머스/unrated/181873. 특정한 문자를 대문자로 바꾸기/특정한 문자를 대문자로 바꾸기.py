def solution(my_string, alp):
    a = list(my_string)
    for i in range(len(a)):
        if a[i] == alp:
            a[i] = a[i].upper()
    return ''.join(a)
