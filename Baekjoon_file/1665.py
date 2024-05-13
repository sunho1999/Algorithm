import heapq
import sys
# input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
left_q, right_q = [], []

for n in nums:
    if len(left_q) == len(right_q):
        heapq.heappush(left_q, (-n, n))
    else:
        heapq.heappush(right_q, (n, n))
    print(left_q," ",right_q)
    if right_q and left_q[0][1] > right_q[0][1]:
        a, b = heapq.heappop(left_q)[1], heapq.heappop(right_q)[1]
        heapq.heappush(left_q, (-b, b))
        heapq.heappush(right_q, (a, a))

    print(left_q[0][1])