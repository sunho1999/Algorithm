import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
edges = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    edges[b].append(a)

def dfs(x):
    visit = [0]*(n+1)
    visit[x] = 1
    stack = [x]
    while stack:
        com = stack.pop()
        for c in edges[com]:
            if not visit[c] :
                visit[c] = 1
                stack.append(c)
    return sum(visit)

com = [dfs(i) for i in range(1, n+1)]
_max = max(com)
for i in range(n):
    if com[i]==_max : print(i+1, end=' ')