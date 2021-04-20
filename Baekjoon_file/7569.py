from collections import deque
M,N,H = map(int,input().split())
#토마토 박스
box = [[]for i in range(H)]
visited = [[[0 for i in range(M)] for i in range(N)] for i in range(H)]
#탐색 할 좌표
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
#큐
que = deque()
for i in range(H):
    for j in range(N):
        a = list(map(int,input().split()))
        box[i].append(a)

#층
for i in range(H):
    #층별 박스 탐색
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                que.append([j,k,i])



#각 층마다 bfs로 탐색
def bfs():
    while que:
        a,b,c,= que.popleft()
        visited[c][a][b] = 1
        for i in range(6):
            kx = dx[i] + a
            ky = dy[i] + b
            kz = dz[i] + c
            if (0 <= kx < N and 0 <= ky < M and 0<= kz < H) and box[kz][kx][ky] == 0 and visited[kz][kx][ky] == 0:
                que.append([kx,ky,kz])
                box[kz][kx][ky] = box[c][a][b]+1
                visited[kz][kx][ky] =1

bfs()
cnt = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                print(-1)
                exit()
            else:
                cnt = max(cnt,box[i][j][k])
print(cnt-1)