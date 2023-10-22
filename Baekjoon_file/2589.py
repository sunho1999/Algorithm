# from collections import  deque
#
# n,m = map(int,input().split())
# mapp=[]
# for i in range(n):
#     mapp.append(list(input().strip("")))
# first_visited = [[0 for _ in range(m)] for _ in range(n)]
# change_mapp = [[0 for _ in range(m)] for _ in range(n)]
# second_visited = [[0 for _ in range(m)] for _ in range(n)]
# second_num = [[0 for _ in range(m)] for _ in range(n)]
#
# def find_idx_bfs(i,j):
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
#     y,x = i,j
#     first_visited[y][x] = 1
#     cnt = 1
#     que = deque()
#     que.append((x,y,cnt))
#
#     while que:
#         x,y,num = que.popleft()
#         change_mapp[y][x] = num
#         for i in range(4):
#             xx = dx[i] + x
#             yy = dy[i] + y
#             if 0<= xx < m and 0<= yy < n:
#                 if first_visited[yy][xx] == 0 and mapp[yy][xx] == "L":
#                     first_visited[yy][xx] = 1
#                     que.append((xx,yy,num+1))
#     return y,x
# check_idx = []
# for i in range(n):
#     for j in range(m):
#         if mapp[i][j] == "L" and first_visited[i][j] == 0:
#             new_y,new_x = find_idx_bfs(i,j) # y,x
#             check_idx.append((new_y,new_x))
# #ex) [(4, 1), (3, 6)]
# def depth_bfs(i,j): # y,x
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
#     y,x = i,j
#     second_visited[y][x] = 1
#     cnt = 1
#     que = deque()
#     que.append((x,y,cnt))
#
#     while que:
#         x,y,num = que.popleft()
#         second_num[y][x] = num
#         for i in range(4):
#             xx = dx[i] + x
#             yy = dy[i] + y
#             if 0<= xx < m and 0<= yy < n:
#                 if second_visited[yy][xx] == 0 and mapp[yy][xx] == "L":
#                     second_visited[yy][xx] = 1
#                     que.append((xx,yy,num+1))
#
# for i in range(len(check_idx)):
#     depth_bfs(check_idx[i][0],check_idx[i][1]) # y,x
# print(second_num)
# max_num = 0
#
# for i in range(len(second_num)):
#     max_num = max(max_num,max(second_num[i]))
#
# print(max_num-1)


import sys;
from collections import deque


def bfs(N, M, r, c):
    Q.append((r, c))
    visited = [[0] * M for _ in range(N)]  # 이 문제의 경우, visited를 bfs 함수 안에 넣어줘야한다.
    visited[r][c] = 1
    sums = 0
    while Q:
        r, c = Q.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r + di, c + dj
            if 0 <= nr < N and 0 <= nc < M:
                if maps[nr][nc] == 'L' and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    sums = max(sums, visited[nr][nc])
                    Q.append((nr, nc))
    return sums - 1


N, M = map(int, sys.stdin.readline().split())

maps = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

Q = deque()
visited = [[0] * M for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        '''
        그냥 map이 L일 때 bfs를 돌리면, 모든 L에 대해 bfs를 돌리기 때문에
        시간 초과가 난다.
        간단한 조건만 걸어주면 된다.
        조건은 map이 L이고 양 옆, 또는 위 아래가 L이 아닐 때 bfs를 돌리면 된다.
        최적의 조건은 아닌 것 같지만 어찌저지 통과는 된다.
        '''
        if maps[i][j] == 'L' and visited[i][j] == 0:
            if 0 <= i - 1 < N and 0 <= i + 1 < N:
                if maps[i - 1][j] == 'L' and maps[i + 1][j] == 'L':
                    continue
            if 0 <= j - 1 < M and 0 <= j + 1 < M:
                if maps[i][j - 1] == 'L' and maps[i][j + 1] == 'L':
                    continue
            result = max(result, bfs(N, M, i, j))

print(result)