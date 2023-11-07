# from collections import  deque
# import  sys
#
# sys.setrecursionlimit(10000000)
# input = sys.stdin.readline
#
# n,m = map(int,input().split())
#
# day = 0
# sum_iceberg = 0
# mapp = []
# visitied = [[0 for _ in range(m)] for _ in range(n)]
# for i in range(n):
#     aa = list(map(int,input().split()))
#     mapp.append(aa)
#
# def check_iceberg(i,j):
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
#     que = deque()
#     que.append((j,i)) # x,y
#     while que:
#         x,y = que.popleft()
#         visitied[y][x] = 1
#         for i in range(4):
#             xx = dx[i] + x
#             yy = dy[i] + y
#             if 0<= xx < m and 0<= yy < n:
#                 if mapp[yy][xx] != 0 and visitied[yy][xx] ==0:
#                     visitied[yy][xx] = 0
#                     que.append([xx,yy])
#     return 1
#
# def mapp_bfs():
#     # print("mapp:",mapp)
#     global day
#     global sum_iceberg
#     global visitied
#     visitied = [[0 for _ in range(m)] for _ in range(n)]
#     day +=1
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
#     check_mapp = [[0 for _ in range(m)] for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             if mapp[i][j] != 0:
#                 cnt = 0
#                 for k in range(4):
#                     xx = dx[k] + j
#                     yy = dy[k] + i
#                     if 0<= xx < m and 0<= yy < n :
#                         if mapp[yy][xx] == 0:
#                             cnt +=1
#                 check_mapp[i][j] = cnt
#                 cnt = 0
#     check = False
#     # print(check_mapp)
#     t = 0
#     for a in range(n):
#         for b in range(m):
#             # print(check_mapp[a][b])
#             if check_mapp[a][b] == 0:
#                 check = True
#             elif check_mapp[a][b] != 0:
#                 check = False
#                 t = 1
#                 break
#         if t ==1:
#             break
#     if check == True:
#         print(0)
#         return
#     for i in range(n):
#         for j in range(m):
#             min_num = min(mapp[i][j],check_mapp[i][j])
#             mapp[i][j] = mapp[i][j] - min_num
#
#     for i in range(n):
#         for j in range(m):
#             if mapp[i][j] != 0 and visitied[i][j] == 0:
#                 num_iceberg = check_iceberg(i,j) # y,x
#                 sum_iceberg += num_iceberg
#
#     if sum_iceberg >= 2:
#         print(day)
#         return
#     else:
#         mapp_bfs()
#
# mapp_bfs() # y,x

import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    seaList = []

    while q:
        x, y = q.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        if sea > 0:
            seaList.append((x, y, sea))
    for x, y, sea in seaList:
        graph[x][y] = max(0, graph[x][y] - sea)

    return 1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

while ice:
    visited = [[0] * m for _ in range(n)]
    delList = []
    group = 0
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if graph[i][j] == 0:
            delList.append((i, j))
    if group > 1:
        print(year)
        break
    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if group < 2:
    print(0)