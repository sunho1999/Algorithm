from sys import stdin
N, M = map(int, stdin.readline().split())
# matrix 배열
matrix = []
for i in range(N):
    matrix.append(list(input()))
# visited 배열
visited = [[0]*M for i in range(N)]
#좌,우,위,아래
dx,dy = [-1,1,0,0], [0,0,-1,1]
#초기 큐
queue = [(0,0)]
#초기 방문
visited[0][0] = 1

#미로탐색 알고리즘
while queue:
    x,y = queue.pop(0)

    if x == N-1 and y == M-1:
        print(visited[x][y])
        break
        
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and matrix[nx][ny] == "1":
                visited[nx][ny] = visited[x][y] +1
                queue.append((nx,ny))

