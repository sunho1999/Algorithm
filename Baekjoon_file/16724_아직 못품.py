import  sys
from collections import  deque
input = sys.stdin.readline
cnt = 0
n,m = map(int,input().split())
matrix = [list(input().strip()) for _ in range(n)]
visited =[[0 for _ in range(m)] for _ in range(n)]

def D(y,x):
    y = y + 1
    x = x
    return (y,x)
def L(y,x):
    x = x -1
    y = y
    return (y, x)
def R(y,x):
    x = x + 1
    y = y
    return (y, x)
def U(y,x):
    x = x
    y = y - 1
    return (y, x)
def dfs(y,x):
    que = deque()
    que.append([y,x])

    while que:
        y,x = que.popleft()
        if visited[y][x] == 0:
            visited[y][x] = 1
            if matrix[y][x] == "D":
                y,x = D(y,x)
                que.append([y,x])
            elif matrix[y][x] == "R":
                y,x = R(y,x)
                que.append([y,x])
            elif matrix[y][x] == "U":
                y,x = U(y,x)
                que.append([y,x])
            elif matrix[y][x] == "L":
                y,x = L(y,x)
                que.append([y,x])
    else:
        return


for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            dfs(i,j)
            print(visited)
            cnt +=1

print(cnt)
