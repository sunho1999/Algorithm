from collections import deque


def bfs(n, m):
    max_size = 100000  # 문제에서 주어진 최대 범위
    visited = [-1] * (max_size + 1)  # 방문 여부 및 도달 시간을 저장
    path = [-1] * (max_size + 1)  # 경로 저장용 배열

    queue = deque([n])
    visited[n] = 0  # 시작 지점 방문 표시

    while queue:
        current = queue.popleft()

        if current == m:
            # 경로를 역추적하여 결과 출력
            print(visited[current])
            result_path = []
            while current != -1:
                result_path.append(current)
                current = path[current]
            print(" ".join(map(str, result_path[::-1])))  # 역순으로 출력
            return

        # 이동 가능한 경우 (X-1, X+1, 2*X)
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= max_size and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1
                path[next_pos] = current  # 어디서 왔는지 기록
                queue.append(next_pos)


# 입력 처리
n, m = map(int, input().split())
bfs(n, m)
