from collections import deque
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n,m = map(int,input().split())

matrix = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

que = deque()
que.append((0,0,0)) # y,x,cnt
dx = [1,-1,0,0]
dy = [0,0,-1,1]

result = 0

def tracking(y,x,cnt):
    # print(dp)
    global result
    result = max(result,cnt)
    if y < 0 or y >= n or x < 0 or x >= m or matrix[y][x] == 'H':
        # print(y,x)
        visited[y][x] = False
        return
    plus_num = int(matrix[y][x])
    for i in range(4):
        xx = plus_num * dx[i] + x
        yy = plus_num * dy[i] + y
        if 0<= xx < m and 0<= yy < n: # 범위 안에 들고
            if matrix[yy][xx] != "H": # 구멍이 아니고
                if dp[yy][xx] < cnt+1: # 탐색할 노드가 기존 노드에서 하나 증가했을때 보다 작을 떄
                    if visited[yy][xx]:
                        print(-1)
                        exit()
                    else:
                        dp[yy][xx] = cnt +1
                        visited[yy][xx] = True
                        tracking(yy,xx,cnt+1)
                        visited[yy][xx] = False

tracking(0,0,0)
print(result+1)

