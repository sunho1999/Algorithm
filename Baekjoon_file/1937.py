from collections import deque
import sys

sys.setrecursionlimit(10**6)
n = int(input())

matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0 for _ in range(n)] for _ in range(n)]

def dfs(a,b):
    if visited[a][b]:
        return visited[a][b]

    visited[a][b] = 1

    for i in range(4):
        x1 = dx[i] + a
        y1 = dy[i] + b
        if 0 <= x1 < n and 0 <= y1 < n:
            #탐색하는 좌표가 현 좌표보다 클 때
            if matrix[x1][y1] > matrix[a][b]:
                visited[a][b] = max(visited[a][b], dfs(x1,y1)+1)
    return visited[a][b]

for i in range(n):
    for j in range(n):
        answer = max(answer,dfs(i,j))
print(answer)