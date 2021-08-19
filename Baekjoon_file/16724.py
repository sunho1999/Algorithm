import  sys
from collections import  deque
input = sys.stdin.readline
cnt = 0
n,m = map(int,input().split())
matrix = [list(input().strip()) for _ in range(n)]
visited =[[0 for _ in range(m)] for _ in range(n)]

check = 1
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
    global cnt
    global check
    que = deque()
    que.append([y,x])
    save =  [y, x] # 첫 방문 좌표 저장
    while que:

        y,x = que.popleft()
        # 첫 방문노드 도착했을 때
        if visited[y][x] == 0:
            #방문노드 저장
            visited[y][x] = check
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

        elif visited[y][x] == check:
            # 다시 싸이클을 돌아 처음 방문했던 좌표에 도착했을 때
            cnt +=1
            return
            # 싸이클을 돌았는데 처음 시작한 싸이클이 아니고 다른 싸이클에 도착했을 때
        elif visited[y][x] != check:
            return

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            dfs(i,j)
            check +=1
print(cnt)
