n,m=map(int,input().split())

r,c,d=map(int,input().split())
graph=[]
for y in range(n):
    graph.append(list(map(int,input().split())))
    
dx=[0,1,0,-1]
dy=[-1,0,1,0]
cnt=0
def bfs(r,c,d):
    global cnt
    if graph[r][c]==0:
        graph[r][c]=2
        cnt+=1
    if graph[r-1][c]!=0 and graph[r+1][c]!=0 and graph[r][c-1]!=0 and graph[r][c+1]!=0:
        r-=dy[d]
        c-=dx[d]
        if graph[r][c]==1:
            print(cnt)
            return
        bfs(r,c,d)
    else:
        while(True):
            d-=1
            if d<0:
                d+=4
            if graph[r+dy[d]][c+dx[d]]==0:
                r+=dy[d]
                c+=dx[d]
                break
        bfs(r,c,d)
        
bfs(r,c,d)