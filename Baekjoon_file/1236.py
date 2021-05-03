import sys
from heapq import heappush, heappop

input = sys.stdin.readline

#마을의 수 , 간선수, 파티마을
n, m, x = map(int, input().split())
inf = 100000000
#기본
s = [[] for i in range(n + 1)]
dp = [inf] * (n + 1)
#역방향
s_r = [[] for i in range(n + 1)]
dp_r = [inf] * (n + 1)

#다익스트라 알고리즘
def dijkstra(start, dp, s):
    heap = []
    dp[start] = 0
    heappush(heap, [0, start])
    while heap:
        #w = 간선 가중치 , n= 노드
        w, n = heappop(heap)
        if dp[n] < w:
            continue
        #정해진 노드 속 연결되어있는 인접 노드 탐색
        for n_n, wei in s[n]:
            #기존 간선가중치와 인접 노드 간선가중치 합
            n_w = wei + w
            # 가중치합이 인접 노드의 가중치합보다 작으면 바꾸기
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])
for i in range(m):
    a, b, t = map(int, input().split())
    s[a].append([b, t])
    s_r[b].append([a, t])
dijkstra(x, dp, s)
dijkstra(x, dp_r, s_r)
max_ = 0

for i in range(1, n + 1):
    max_ = max(max_, dp[i] + dp_r[i])
print(max_)