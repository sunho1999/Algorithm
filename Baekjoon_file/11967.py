from collections import deque


def bfs():
    need_visited = deque([(1, 1)])
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [[False] * (n + 1) for _ in range(n + 1)]
    graph[1][1] = 1
    visited[1][1] = True
    ans = 1

    while need_visited:
        x, y = need_visited.popleft()

        # 미방문 인접 노드 중 아직 불이 안켜진 방은 넘어가기
        if graph[x][y] == 0:
            continue

        # 현재 방에서 켤 수 있는 불 다 켜기
        if (x, y) in light.keys():
            for a, b in light[(x, y)]:
                if graph[a][b] == 0:
                    graph[a][b] = 1
                    ans += 1
            del light[(x, y)]

        # 인접한 방으로 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx <= n and ny <= n and nx > 0 and ny > 0 and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    need_visited.appendleft((nx, ny))
                    # 미방문 인접 노드는 queue 뒤쪽에 추가
                else:
                    need_visited.append((nx, ny))
    return ans


n, m = map(int, input().split())
light = {}

for _ in range(m):
    x, y, a, b = map(int, input().split())
    if (x, y) not in light.keys():
        light[(x, y)] = [(a, b)]
    else:
        light[(x, y)] += [(a, b)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

print(bfs())