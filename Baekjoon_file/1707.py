import sys
from collections import  deque
sys.setrecursionlimit(10000000)
testcase = int(input())

def bfs(start):
    que = deque()
    que.append(start)
    visit[start] = 1

    while que:
        a = que.popleft()
        for i in matrix[a]:
            if visit[i] == 0:
                visit[i] = -visit[a]
                que.append(i)
            else:
                if visit[i] == visit[a]:
                    return False
    return True


for i in range(testcase):
    check = True
    #v 정점 개수, e 간선개수
    v,e = map(int,input().split())
    #방문 정점 체크
    visit = [0 for _ in range(v+1)]
    #링크드리스트
    matrix = [[] for _ in range(v+1)]
    for j in range(e):
        a,b = map(int,sys.stdin.readline().split())
        matrix[a].append(b)
        matrix[b].append(a)
    for k in range(1,v+1):
        if visit[k] == 0:
            check = bfs(k)
            if check == False:
                break
    print("YES" if check else "NO")