import sys
testcase = int(sys.stdin.readline())

def solve_bf(bf, graph, n, m):
    bf[1] = 0
    for it in range(n):
        for v in range(1, n+1):
            for nv, nw in graph[v]:
                if bf[nv] > bf[v] + nw:
                    bf[nv] = bf[v] + nw
                    if it == n-1:
                        print("YES")
                        return
    print("NO")
    return

for _ in range(testcase):
    n, m, w = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    bf = [1e9] * (n+1)
    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        graph[s].append([e, t])
        graph[e].append([s, t])
    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().split())
        graph[s].append([e, -t])
    solve_bf(bf, graph, n, m)