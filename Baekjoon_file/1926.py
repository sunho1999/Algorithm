from collections import deque
n,m = map(int,input().split())

mapp = []
for i in range(n):
    mapp.append(list(map(int,input().split())))
visited = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0
def bfs(i,j):
    que = deque()
    check_num = 0
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    que.append((j,i))
    while que:
        x,y = que.popleft()
        if visited[y][x] == 1:
            pass
        else:
            check_num +=1
            visited[y][x] = 1
            for i in range(4):
                xx = dx[i] + x
                yy = dy[i] + y
                if 0<= xx < m and 0<= yy < n:
                    if mapp[yy][xx] == 1 and visited[yy][xx] == 0:
                        que.append((xx,yy))
    return check_num

answer_list = []
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and mapp[i][j] == 1:
            a = bfs(i,j) # y,x
            cnt +=1
            answer_list.append(a)

if len(answer_list) == 0:
    print(cnt)
    print(0)
else:
    print(cnt)
    print(max(answer_list))
