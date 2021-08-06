import sys
sys.setrecursionlimit(1000000)
n, m = map(int, input().split())

matrix = [[] for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

visited = [0 for i in range(n)]

def dfs(start, depth):
    global ans
    visited[start] = True
    if depth == 4:
        ans = True
        return
    for i in matrix[start]:
        if not visited[i]:
            dfs(i, depth+1)
            visited[i] = False

ans = False
# 돌아가면서 dfs의 시작점 설정
for i in range(n):
    dfs(i,0)
    visited[i] = False
    if ans:
        break
print(1 if ans else 0)