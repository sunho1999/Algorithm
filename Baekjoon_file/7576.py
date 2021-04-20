import sys
from collections import deque
m,n = map(int,sys.stdin.readline().split())
#토마토 상자
que = deque()
matrix = []
for i in range(n):
    matrix.append(list(map(int,sys.stdin.readline().split())))


dx = [1,-1,0,0]
dy = [0,0,-1,1]
#1이 있는 좌표 que에 담기
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            que.append([i,j])

#bfs로 1에 있는 인접좌표 0이면 바꾸기 바꾸면서 day +=1
def bfs():
    day = -1
    while que:
        day+=1
        a, b = que.popleft()
        for i in range(4):
            x = dx[i] + a
            y = dy[i] + b
            if (0 <= x < n) and (0 <= y < m) and (matrix[x][y] == 0):
                matrix[x][y] = matrix[a][b]+1
                que.append([x,y])

bfs()
isTrue = False
result = -2
#첫번쨰줄 상자 부터 접근해서 맥스 값 따오기
for i in matrix:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)
#상자 값중에 0이있으면 -1 출력
if isTrue == True:
    print(-1)
#상자 값중에 1이 최대값이면 0출력
elif result == -1:
    print(0)
#상자 값 중에 제일 높은값 -1 출력 > 기존 1이 담겨있어서 카운트를 하면 안됨.
else:
    print(result - 1)

