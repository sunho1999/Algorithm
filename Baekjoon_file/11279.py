import heapq
import sys

n = int(sys.stdin.readline())

heap = []

for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print("0")
    else:
        heapq.heappush(heap,[-a,a])
