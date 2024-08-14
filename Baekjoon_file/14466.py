from collections import deque
import sys

input =sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(y,x):
    y -=1
    x -=1
    que = deque()
    que.append((y,x))
    cow_visited[y][x] = 1
    while que:
        y,x = que.popleft()
        for i in range(4):
            yy = dy[i] + y
            xx = dx[i] + x
            if 0 <= xx < n and 0<= yy < n:
                if cow_visited[yy][xx] == 0:
                    if (yy,xx) not in road[y][x]:
                        que.append((yy,xx))
                        cow_visited[yy][xx] = 1

n,k,r = map(int,input().split())
count =0
# 다리
road = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(r):
    r1, c1, r2, c2 = map(int,input().split())
    road[r1 - 1][c1 - 1].append((r2 - 1, c2 - 1))
    road[r2 - 1][c2 - 1].append((r1 - 1, c1 - 1))

# 소 위치
cow_idx = [list(map(int,input().split())) for _ in range(k)]

for i,idx in enumerate(cow_idx):
    # 소 방문 여부
    cow_visited = [[False] * n for _ in range(n)]
    bfs(idx[0],idx[1])
    for y,x in cow_idx[i+1:]:
        if not cow_visited[y-1][x-1]:
            count +=1
print(count)