from collections import deque

n,m = map(int,input().split())
visitied = [[0 for _ in range(m)] for _ in range(n)]
new_map = [[0 for _ in range(m)] for _ in range(n)]
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))

def bfs(i,j,cnt):
    que = deque()
    que.append((j,i,cnt)) # x,y
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while que:
        x,y,num = que.popleft()
        if visitied[y][x] == 1:
            continue
        visitied[y][x] = 1
        new_map[y][x] = num
        # print(num)
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < m and 0 <= next_y < n:
                if visitied[next_y][next_x] == 0 and matrix[next_y][next_x] == 1:
                    que.append((next_x,next_y,num+1))

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            bfs(i,j,0)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and new_map[i][j] == 0:
            new_map[i][j] = -1

for i in range(n):
    for j in range(m):
        print(new_map[i][j], end = " ")
    print()

