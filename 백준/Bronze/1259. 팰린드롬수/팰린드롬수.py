while True:
    s = list(input())
    if s == ['0']: break
    
    if all(s[i] == s[-(i+1)] for i in range(len(s) // 2)):
        print('yes')
    else: print('no')