def solution(s):
    len1= len(s)
    count0 = 0
    cnt = 0
    while int(s) != 1:
        cnt += 1
        len0 = str(s).count("0")
        s = str(s).count("1")
        count0 += len0
        s= bin(s)[2:]
    return [cnt,count0]