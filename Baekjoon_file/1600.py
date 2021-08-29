from collections import deque

horse_x = [-2, -2, -1, 1, 2, 2, -1, 1]
horse_y = [-1, 1, -2, -2, -1, 1, 2, 2]

monkey_x = [-1, 0, 1, 0]
monkey_y = [0, -1, 0, 1]
def sol():
    ck = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]

    while que:
        x, y, k = que.popleft()
        if x == (H-1) and y == (W-1):
            return ck[x][y][k]
        for i in range(4):
            mx = x + monkey_x[i]
            my = y + monkey_y[i]
            if mx < 0 or mx >= H or my < 0 or my >= W:
                continue
            if ck[mx][my][k] or Map[mx][my]:
                continue
            ck[mx][my][k] = ck[x][y][k] + 1
            que.append([mx, my, k])
        if k == K:
            continue
        for i in range(8):
            dx = x + horse_x[i]
            dy = y + horse_y[i]
            if dx < 0 or dx >= H or dy < 0 or dy >= W:
                continue
            if ck[dx][dy][k+1] or Map[dx][dy]:
                continue
            ck[dx][dy][k+1] = ck[x][y][k] + 1
            que.append([dx, dy, k+1])
    return -1
# 말 이동횟수
K = int(input())
W, H = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(H)]
que = deque()
que.append([0, 0, 0])
print(sol())
