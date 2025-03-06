from collections import deque

n = int(input())
mapp = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 1, 0]  # 가로, 대각선, 세로 이동
dy = [0, 1, 1]
now = [0, 1, 2]  # 0: 가로, 1: 대각선, 2: 세로

# DP 테이블 (경로 개수 저장)
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

# BFS 큐 생성
que = deque([(0, 1, 0)])  # (y, x, 방향)
dp[0][1][0] = 1  # (0,1)에서 가로 방향 시작

def bfs():
    while que:
        y, x, pipe_now = que.popleft()

        for i in range(3):  # 3가지 방향 이동
            if abs(i - pipe_now) > 1:
                continue  # 가로↔세로 직접 변경 불가

            yy, xx = y + dy[i], x + dx[i]

            if 0 <= yy < n and 0 <= xx < n and mapp[yy][xx] == 0:  # 벽이 아닐 때
                if i == 1:  # 대각선 이동 시 추가 검사
                    if mapp[y][x+1] == 1 or mapp[y+1][x] == 1:
                        continue  # 대각선 이동 불가

                # 새로운 위치에 대해 기존 경로 개수를 더함 (DP 적용)
                dp[yy][xx][i] += dp[y][x][pipe_now]

                # 큐에 새로운 상태 추가
                que.append((yy, xx, i))

bfs()
print(sum(dp[n-1][n-1]))  # (n-1, n-1)에 도착하는 모든 경우의 수 합산
