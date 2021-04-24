from collections import deque

def bfs(i,j):

    que.append((i,j))
    visited[i][j] = cnt
    while que:
        a, b = que.popleft()
        #좌표 탐색
        for i in range(4):
            x = dx[i] + a
            y = dy[i] + b
            if 0 <= x < n and 0 <= y < n :
                if visited[x][y] ==0 and list[x][y] == list[a][b]:
                    que.append((x,y))
                    visited[x][y] = 1

n = int(input())
list = [list(input()) for i in range(n)]
que = deque()
cnt = 0
#좌표 탐색 리스트
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#그냥 정상 탐
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            cnt +=1
print(cnt,end =' ')


#적록 리스트 복사
for i in range(n):
    for j in range(n):
        if list[i][j] == 'G':
            list[i][j] = 'R'

#적록색맹 탐색
visited = [[0]*n for i in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 :
            bfs(i,j)
            cnt +=1


print(cnt)