from collections import deque
import sys

# J와 F동시에 BFS시작
# 탐색한 좌표를 담을 수 있는 변수 x 필요
    # 해당 변수에 J와 F를 구분할 수 있는 변수 필요
# 좌표를 담은 변수x를 pop하며 탐색 진행
# 탐색을 한 후, 다시 x에 저장, 이때 카운티 1증가
# J가 F랑 곂치면 임파서블 출력
# J가 벽 외각에 도달하면 cnt 출력

r,c = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = "IMPOSSIBLE"
def bfs():
    global answer
    while que:
        # print(mapp)
        y,x,time = que.popleft()
        if time >= 1 and mapp[y][x]!= "F" and (y==0 or x == 0 or y == r-1 or x ==c-1):
            answer = time
            return
            # break
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0<= yy < r and 0<= xx < c:
                if mapp[yy][xx] != "#": #벽이 아닐 때
                    if time >= 1 and mapp[yy][xx] == ".": # pop한게 지훈이 일때
                        mapp[yy][xx] = "@" # 방문 체크
                        que.append((yy,xx,time+1))
                    elif time == 0 and mapp[yy][xx] != "F": # pop한게 불일 때
                        mapp[yy][xx] = "F" # 불 번짐
                        que.append((yy,xx,0))
mapp = [list(input()) for _ in range(r)]
que = deque()
for i in range(r):
    for j in range(c):
        if mapp[i][j] == "J":
            que.append((i,j,1)) # y,x,time
for i in range(r):
    for j in range(c):
        if mapp[i][j] == "F":
            que.append((i,j,0)) # y,x,time
bfs()
print(answer)