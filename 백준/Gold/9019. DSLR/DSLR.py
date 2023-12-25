from collections import deque
import sys
read = sys.stdin.readline

def bfs(A,B):
    Q = deque()
    visited1 = [""] * 10000
    visited2 = [""] * 10000
    
    Q.append((A,1))
    visited1[A] = ""
    Q.append((B,2))
    visited2[B] = ""

    while len(Q)>0:
        num, type = Q.popleft()

        if type == 1:
            for cmd in ['D','S','L','R']:
                if cmd == 'D':
                    if num == 0:
                        continue
                    nxt_num = (num*2) % 10000
                elif cmd == 'S':
                    nxt_num = num-1 if num != 0 else 9999
                elif cmd == 'L':
                    nxt_num = (num % 1000) * 10 + num//1000
                elif cmd == 'R':
                    nxt_num = (num%10) * 1000 + num//10
                
                if visited1[nxt_num] == ""and nxt_num != num:
                    Q.append((nxt_num,type))
                    visited1[nxt_num] = visited1[num] + cmd
                
                if nxt_num == B:
                    return visited1[nxt_num]
                elif visited1[nxt_num] != "" and visited2[nxt_num] != "":
                    return visited1[nxt_num] + visited2[nxt_num]
        else: # type == 2:
            for cmd in ['R', 'L', 'S','D2','D']:
                if cmd == 'D':
                    if num %2 != 0:
                        continue
                    nxt_num = (num + 10000) //2
                elif cmd == 'D2':
                    if num %2 != 0:
                        continue
                    cmd = 'D'
                    nxt_num = num // 2
                elif cmd == 'S':
                    nxt_num = 0 if num == 9999 else num + 1
                elif cmd == 'L':
                    nxt_num = (num%10) * 1000 + num//10
                elif cmd == 'R':
                    nxt_num = (num % 1000) * 10 + num//1000
                
                if visited2[nxt_num] == "" and nxt_num != num:
                    Q.append((nxt_num,type))
                    visited2[nxt_num] = cmd + visited2[num]
                
                if visited1[nxt_num] != "" and visited2[nxt_num] != "":
                    return visited1[nxt_num] + visited2[nxt_num]

def main():
    T = int(read().strip())
    for _ in range(T):
        A, B = map(int,read().rstrip().split())
        res = ""
        if A!=B:
            res = bfs(A,B)
        print(res)

if __name__ == '__main__':
    main()
