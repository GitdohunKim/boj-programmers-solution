
import sys
input = sys.stdin.readline

T = int(input())

distance= [0] *(T+1)

def power_numebr(D):

    q = 1

    while(True):
        if(q*q > D):
            q = q-1
            break
        else:
            q= q+1
    
    return q

count = 0

for i in range(1,T+1):
    x,y = map(int,input().split())
    distance[i] = y-x
    
for k in range(1,T+1):
    number = power_numebr(distance[k])
    count = number + number-1
    if(distance[k] == number**2):
        print(count)
        continue
    else:
        dist = distance[k] - number**2
        while(dist!=0):
            count = count + dist // number
            dist = dist % number
            number = number -1

        print(count)
                