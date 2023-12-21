from bisect import bisect_left, bisect_right

def crange(a, lv,rv):
    ri = bisect_right(a,rv)
    li = bisect_left(a,lv)
    return ri-li

array = [[] for _ in range(10001)]
rarray = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        rarray[len(word)].append(word[::-1])
        
    for  i in range(10001):
        array[i].sort()
        rarray[i].sort()
    
    for q in queries:
        if q[0] != '?':
            res = crange(array[len(q)],q.replace('?','a'),q.replace('?','z'))
        else:
            res = crange(rarray[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','z'))
        answer.append(res)
    return answer