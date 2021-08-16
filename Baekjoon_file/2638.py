import sys
from collections import deque
input = sys.stdin.readline
#세로,가로
n,m = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

matrix = [list(map(int,input().split())) for _ in range(n)]


def bfs():
    que = deque()
    visited = [[-1] * m for _ in range(n)] #bfs 실행할때마다 visited  초기화
    que.append([0,0])
    visited[0][0] = 0

    while que:
        x,y = que.popleft()
        for i in range(4):
            x1 = dx[i] + x
            y1 = dy[i] + y
            # 최대 인덱스 까지 접근 허용
            if 0 <= x1 < n and 0 <= y1 < m:
                # 방문한 인덱스가 처음일때
                if visited[x1][y1] == -1:
                    if matrix[x1][y1] >= 1: # 이때 방문한 인덱스가 치즈일때
                        matrix[x1][y1] +=1  #1증가
                    else: # 방문한 인덱스가 공기일때
                        visited[x1][y1] = 0 #방문한 인덱스 체크
                        que.append([x1,y1]) #탐색한 인덱스 que에 넣기

answer =0

while True:
    # 치즈가 공기에 맞닿아 녹을때마다 bfs 실행
    bfs()
    cnt = 0
    for i in range(n):
        for j in range(m):
            # 녹을 치즈가 있으면 치즈 녹이고 count 1증가
            if matrix[i][j] >= 3:
                matrix[i][j] = 0
                cnt = 1
            # 치즈 안에 있어서 녹지 않은 치즈가 있으면 1로 다시 초기화
            elif matrix[i][j] == 2:
                matrix[i][j] = 1
    if cnt == 1:
        answer += 1
    else:
        break

print(answer)
