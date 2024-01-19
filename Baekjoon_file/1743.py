from collections import deque
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline



n,m,k = map(int,input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(k):
    y,x = map(int,input().split())
    matrix[y-1][x-1] = 1

def dfs(y,x):
    que = deque()
    que.append((y,x))
    cnt = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while que:
        # print(y,x)
        y,x = que.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if 0<= xx < m and 0<= yy < n:
                if matrix[yy][xx] != 0 and visited[yy][xx] ==0:
                    visited[yy][xx] = 1
                    cnt +=1
                    que.append((yy,xx))
    return cnt

answer = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            num1 = dfs(i,j)
            answer.append(num1)
print(max(answer))
