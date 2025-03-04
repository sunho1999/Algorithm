from collections import deque  # Queue
import sys
input = sys.stdin.readline

testcase = int(input())  # 테스트케이스
for _ in range(testcase):
    N, M = map(int, input().split())   # N, M 입력 받기
    numbers = list(map(int, input().split()))  # 초기 큐 입력 받기
    que = deque()
    for i in range(N):
        que.append((numbers[i], i))  # 우선순위, 초기 위치 큐에 삽입

    idx = 1  # 출력 순서
    numbers.sort(reverse=True)  # 우선순위가 큰 값부터 출력하므로 내림차순 정렬

    while que:
        q = que.popleft()
        if q[0] == numbers[idx-1]:  # 꺼낸 값이 남은 값중 최대값일 때
            if q[1] == M:  # 찾는 위치의 값일 때
                print(idx)
                break
            idx += 1  # 최대값 업데이트
        else:
            que.append(q)  # 최대값이 아닐 때 큐의 맨 뒤로 삽입