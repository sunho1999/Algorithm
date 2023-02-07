from collections import deque

N, L, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

is_move = False

def bfs(x, y, visited, matrix):
    global is_move
    people = matrix[x][y]
    count = 1
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    temp = list()
    temp.append((x,y))

    while queue:
        pop_x, pop_y = queue.popleft()

        for i in range(4):
            ax = pop_x + dx[i]
            ay = pop_y + dy[i]

            if ax >= 0 and ax < N and ay >=0 and ay < N:
                if visited[ax][ay] == 0:
                    if L <= abs(matrix[pop_x][pop_y] - matrix[ax][ay]) <= R:
                        visited[ax][ay] = 1
                        queue.append((ax, ay))
                        people += matrix[ax][ay]
                        count += 1
                        temp.append((ax, ay))
    move_people = people // count

    if count > 1:
        is_move = True
        for xx, yy in temp:
            matrix[xx][yy] = move_people

answer = 0

while True:
    is_move = False
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0: # 방문하지 않은 노드
                bfs(i, j, visited, matrix)
    if is_move:
        answer += 1
    else:
        break
print(answer)