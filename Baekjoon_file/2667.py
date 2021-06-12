from collections import deque

n = int(input())

matrix = [list(map(int,input().strip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)] #탐색 좌표 체크 0이면 방문 x , 1이면 방문 o
answer = [] #단지 수 넣을 값

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    que = deque()
    cnt = 1
    que.append([a,b])
    while que:
        t,h = que.popleft() #큐에 있는 좌표 빼내기
        visited[t][h] = 1
        for i in range(4):
            x = dx[i] + t
            y = dy[i] + h
            if (0<= x < n and 0<= y < n):
                if (matrix[x][y] == 1 and visited[x][y] == 0):
                    visited[x][y] = 1
                    cnt +=1
                    que.append([x,y])
    answer.append(cnt)


for i in range(n):
    for j in range(n):
        if matrix[i][j] ==1 and visited[i][j] == 0:
            a,b = i,j
            bfs(a,b)

answer.sort()
print(len(answer))
for i in answer:
    print(i)