import sys
import heapq

n = int(sys.stdin.readline())
heap =[]

for i in range(n):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(heap,a)
    else:
        if len(heap) ==0:
            print(0)
        else:
            print(heapq.heappop(heap))
