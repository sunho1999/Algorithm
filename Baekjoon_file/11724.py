import sys
sys.setrecursionlimit(10000)
def dfs(v):
    visited[v] = 1
    for m in range(1,N+1):
        if visited[m] ==0 and matrix[v][m] == 1:
            dfs(m)

N,M = map(int,sys.stdin.readline().split())

matrix = [[0]*(N+1) for i in range(N+1)]
cnt = 0
visited = [0]*(N+1)
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1


for i in range(1,N+1):
    if visited[i] == 0:
        dfs(i)
        cnt +=1

print(cnt)