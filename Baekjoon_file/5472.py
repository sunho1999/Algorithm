import sys
from collections import deque

input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

testcase = int(input())


def bfs(f_s, queue, visit):
    while queue:
        y, x, time = queue.popleft()
        # print(y,x)
        for i in range(4):
            yy = dy[i] + y
            xx = dx[i] + x
            if 0 <= yy < h and 0 <= xx < w:
                if mapp[yy][xx] == "." or mapp[yy][xx] == "@":
                    if visit[yy][xx] > time + 1:
                        visit[yy][xx] = time + 1
                        queue.append((yy, xx, visit[yy][xx]))
            else:
                if f_s == 's':  # 상근이면 w, h를 벗어나는 순간 스탑
                    print(time + 1)
                    return
    # print(mapp)
    if f_s == 's':
        print("IMPOSSIBLE")

for i in range(testcase):
    mapp = []
    w,h = map(int,input().split())
    visit = [[1e9 for _ in range(w)] for _  in range(h)]

    escape_idx = []
    human_idx = deque()
    fire_idx = deque()
    for i in range(h):
        mapp.append(list(input()))

    for j in range(h):
        for k in range(w):
            if mapp[j][k] == "*":
                fire_idx.append((j,k,0))
                visit[j][k] = 0
            elif mapp[j][k] == "@":
                human_idx.append((j,k,0))

   # 불 먼저 bfs
    bfs('f', fire_idx, visit)
    bfs('s', human_idx, visit)
    # print(visit)