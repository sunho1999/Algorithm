import sys
from collections import deque


dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]
que = deque()

def bfs(i,j):
    test_case[i][j] = 0
    que.append([i,j])
    while que:
        a,b = que.popleft()
        for c in range(8):
            x = dx[c] + a
            y = dy[c] + b
            if 0<= x < h and 0<= y < w and test_case[x][y] == 1:
                test_case[x][y] = 0
                que.append([x,y])

while True:
    w,h = map(int,sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    else:
        test_case = []
        cnt = 0
        for i in range(h):
            test_case.append(list(map(int,input().split())))
        for i in range(h):
            for j in range(w):
                if test_case[i][j] ==1:
                    bfs(i,j)
                    cnt +=1
    print(cnt)