from collections import  deque
import sys
input = sys.stdin.readline
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]
q1 = deque()


#각 영역 분리하기(cnt증가하면서)
def bfs1(i,j):
    global cnt
    q1.append([i,j])
    matrix[i][j] = cnt
    visited1[i][j] = 0
    while q1:
        x,y = q1.popleft()

        for i in range(4):
            dx1 = x + dx[i]
            dy1 = y + dy[i]
            if 0 <= dx1 < n and 0 <= dy1 < n:
                if matrix[dx1][dy1] == 1 and visited1[dx1][dy1] == 0:
                    matrix[dx1][dy1] = cnt
                    visited1[dx1][dy1] = 1
                    q1.append([dx1,dy1])


visited1 = [[0] * n for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and visited1[i][j] == 0:
            bfs1(i,j)
            cnt +=1


def bfs2(count):
    q2 = deque()
    global answer
    # 거리 늘려가면서 방문 노드 저장할 리스트
    visited2 = [[-1]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == count:
                q2.append([i,j])
                visited2[i][j] = 0
    while q2:
        x,y = q2.popleft()
        for i in range(4):
            dx1 = x + dx[i]
            dy1 = y + dy[i]

            if dx1 < 0 or dx1 >= n or dy1 < 0 or dy1 >= n:
                continue
            if matrix[dx1][dy1] > 0 and matrix[dx1][dy1] != count:
                answer = min(answer,visited2[x][y])
                return
            if matrix[dx1][dy1] == 0 and visited2[dx1][dy1] == -1:
                visited2[dx1][dy1] = visited2[x][y] + 1
                q2.append([dx1,dy1])

answer = sys.maxsize

for i in range(1,cnt):
    bfs2(i)

print(answer)

