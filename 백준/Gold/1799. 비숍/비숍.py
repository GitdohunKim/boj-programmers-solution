import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
n = int(input())


table = [list(map(int,input().split())) for _ in range(n)]
black_table = [t[:] for t in table]
white_table = [t[:] for t in table]
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            black_table[i][j] = 0
        else:
            white_table[i][j] = 0

shop = deque()





def check(x,y):
    for a , b in shop:
        if abs(x - a) == abs(y - b) : return False

    return True


answer = 0
def back_track1(x,y):
    global answer
    if x == n -1 and y == n -1 :
        answer = max(answer , len(shop))

    elif x == n:
        back_track1(0,y+1)
    else:
        if black_table[x][y] == 1 and check(x,y):
            shop.append((x,y))
            back_track1(x+1,y)
            shop.pop()
            back_track1(x+1,y)
        else:
            back_track1(x+1,y)

back_track1(0,0)

def back_track2(x,y):
    global answer2
    if x == n and y == n -1 :
        answer2 = max(answer2 , len(shop))

    elif x == n:
        back_track2(0,y+1)
    else:
        if white_table[x][y] == 1 and check(x,y):
            shop.append((x,y))
            back_track2(x+1,y)
            shop.pop()
            back_track2(x+1,y)
        else:
            back_track2(x+1,y)
answer2 = 0
shop = deque()
back_track2(0,0)

print(answer + answer2)