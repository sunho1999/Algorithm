n = int(input())

import sys
sys.setrecursionlimit(10000000)
d = [10, 30, 5, 60]
M = [[0 for x in range(len(d))] for y in range(len(d))]
for diag in range(1, len(d)):
    for i in range(1, len(d) - diag):
        j = i + diag
        M[i][j] = sys.maxsize
        for k in range(i, j):
            M[i][j] = min(M[i][j],
                          M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j])

print(M[1][d[-1]])
