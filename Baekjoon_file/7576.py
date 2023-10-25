import sys
from collections import deque

input = sys.stdin.readline

M,N = map(int,input().split()) #가로, 세로

visited = [[0 for _ in range(M)] for _ in range(N)]
matrix = [list(map(int,input().split())) for _ in range(N)]

que = deque()

for i in range(N): #세로
    for j in range(M):  #가로
        if matrix[i][j] == 1:
            que.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 1
while que:
    x,y = que.popleft()
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        if 0 <= ax < N  and 0<= ay < M:
            if matrix[ax][ay] == 0 :
                matrix[ax][ay] = matrix[x][y] + 1
                que.append((ax,ay))

max_value = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            print(-1)
            exit()
    if max(matrix[i]) > max_value:
        max_value = max(matrix[i])

print(max_value-1)