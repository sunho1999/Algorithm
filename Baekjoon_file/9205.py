# 맥주 한 박스에는 맥주가 20개 들어있다. 목이 마르면 안되기 때문에 50미터에 한 병씩 마시려고 한다. 즉, 50미터를 가려면 그 직전에 맥주 한 병을 마셔야 한다.
# 편의점에 들렸을 때, 빈 병은 버리고 새 맥주 병을 살 수 있다. 하지만, 박스에 들어있는 맥주는 20병을 넘을 수 없다. 편의점을 나선 직후에도 50미터를 가기 전에 맥주 한 병을 마셔야 한다.
from collections import deque

def bfs():
    que = deque()
    que.append((home_idx_x,home_idx_y))

    while que:
        x,y = que.popleft()
        if abs(x-festival_idx_x) + abs(y-festival_idx_y) <= 1000:
            print("happy")
            return
        else:
            for i in range(store_cnt):
                if visited[i] == False:
                    xx = store_idx_list[i][0]
                    yy = store_idx_list[i][1]
                    if abs(xx-x) + abs(yy-y) <= 1000:
                        visited[i] = True
                        que.append((xx,yy))
    print('sad')
    return

testcase = int(input())

for _ in range(testcase):
    store_cnt = int(input())
    home_idx_x, home_idx_y = map(int,input().split())
    store_idx_list = []
    for i in range(store_cnt):
        store_idx_x, store_idx_y = map(int,input().split())
        store_idx_list.append((store_idx_x, store_idx_y)) # x,y
    festival_idx_x, festival_idx_y = map(int,input().split())
    visited = [False for _ in range(store_cnt+1)]
    bfs()