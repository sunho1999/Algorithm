from collections import deque
# F, S, G, U, D가 주어진다.
F, S, G, U, D = map(int,input().split())
# F : 스타트링크 건물 층수
# S : 있는 위치
# G : 스타트링크 있는 위치
# U : 위로 갈수 있는 층
# D : 아래로 갈수 있는 층

dp = [99999999 for _ in range(F+1)]
visited = [0 for _ in range(F+1)]
def DFS(s):
    visited[s] = 1
    dp[s] = 1
    que = deque()
    que.append(s)
    while que:
        s = que.popleft()
        up_s = s + U
        down_s = s - D
        # print(up_s,down_s)
        if up_s <= F:
            if visited[up_s] == 0:
                dp[up_s] = min(dp[up_s],dp[s] +1)
                visited[up_s] = 1
                que.append(up_s)
        if down_s > 0:
            if visited[down_s] == 0:
                dp[down_s] = min(dp[down_s],dp[s] + 1)
                visited[down_s] = 1
                que.append(down_s)
    return
DFS(S)

if dp[G] == 99999999:
    print("use the stairs")
else:
    print(dp[G]-1)