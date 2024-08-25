from collections import deque

n, m = map(int, input().split())
input_matrix = [list(map(int, input().split())) for _ in range(n)]
answer = [[-1 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]
que = deque()

# 상어가 있는 모든 위치를 큐에 넣고 시작
for i in range(n):
    for j in range(m):
        if input_matrix[i][j] == 1:
            que.append((i, j))
            answer[i][j] = 0

while que:
    y, x = que.popleft()
    current_distance = answer[y][x]

    for i in range(8):
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 <= yy < n and 0 <= xx < m:
            # 아직 방문하지 않았거나 더 짧은 거리를 찾은 경우
            if answer[yy][xx] == -1 or answer[yy][xx] > current_distance + 1:
                answer[yy][xx] = current_distance + 1
                que.append((yy, xx))

# 최댓값 구하기
max_distance = max(max(row) for row in answer)
print(max_distance)
