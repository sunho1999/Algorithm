import collections
import sys

n,m = map(int,sys.stdin.readline().split())
list1 = [[0]*(n+1)]

#매트릭스 만들기
for _ in range(n):
    nums = [0] + [int(x) for x in sys.stdin.readline().split()]
    list1.append(nums)


# 행 별로 더하기
for i in range(1, n + 1):
    for j in range(1, n):
        list1[i][j + 1] += list1[i][j]

# 열 별로 더하기
for j in range(1, n + 1):
    for i in range(1, n):
        list1[i + 1][j] += list1[i][j]


for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(list1[x2][y2] - list1[x1 - 1][y2] - list1[x2][y1 - 1] + list1[x1 - 1][y1 - 1])

