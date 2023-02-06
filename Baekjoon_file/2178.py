import sys
from collections import deque
input = sys.stdin.readline


dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs():
    que = deque()
    que.append((0,0))
    while que:
        y,x = que.popleft()
        if y == N-1 and x == M-1:
            print(visited[y][x] + 1)
            break
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if (ax >=0 and ax < M) and (ay >= 0 and ay < N):
                if matrix[ay][ax] == "1" and visited[ay][ax] ==0:
                    visited[ay][ax] = visited[y][x] + 1
                    que.append((ay,ax))


N,M = map(int,input().split())

matrix = [list(input().strip()) for i in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

bfs()
