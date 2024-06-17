import heapq, sys
input = sys.stdin.readline
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
array.sort(key = lambda x: x[1])
min_h = []
count = 0
for x in array:
    while min_h and min_h[0] <= x[1]:
        heapq.heappop(min_h)
    heapq.heappush(min_h, x[2])
    count = max(count, len(min_h))
print(count)