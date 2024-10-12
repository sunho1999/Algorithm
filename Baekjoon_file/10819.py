from itertools import permutations
import sys

# 주어진 값 입력
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

per = permutations(a)
ans = 0

for i in per:
    s = 0
    for j in range(len(i) - 1):
        s += abs(i[j] - i[j + 1])
    if s > ans:
        ans = s

print(ans)