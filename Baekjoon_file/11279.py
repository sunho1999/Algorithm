import heapq
import sys

<<<<<<< HEAD
N = int(sys.stdin.readline())

heap = []

for i in range(N):
=======
n = int(sys.stdin.readline())

heap = []

for i in range(n):
>>>>>>> 902afb7ae9b2b2c8ac36873864403c6ce48f2d1f
    a = int(sys.stdin.readline())
    if a == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print("0")
    else:
        heapq.heappush(heap,[-a,a])
