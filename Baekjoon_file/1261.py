from collections import deque
import sys
sys.setrecursionlimit(10000000)
n,m = map(int,input().split())

visited = [[0 for _ in range(n)] for _ in range(m)] #1,1 부터 좌표 시작
matrix = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(m):
    matrix.append(list(map(int,input().strip())))


def bfs(a,b):
    que = deque()
    que.append([a,b])
    visited[a][b] = 1
    while que:
        a,b = que.popleft()
        for i in range(4):
            x = dx[i] + a
            y = dy[i] + b
            if 0 <= x < m and 0 <= y < n:
                if matrix[x][y] == 0 and visited[x][y] == 0:
                     visited[x][y] = visited[a][b]
                     que.appendleft([x,y])
                elif matrix[x][y] == 1 and visited[x][y] ==0:
                    visited[x][y] = visited[a][b] + 1
                    que.append([x,y])

bfs(0,0)
print(visited[-1][-1]-1)