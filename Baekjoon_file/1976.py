from collections import deque

n = int(input())
m = int(input())

city = []

for i in range(n):
    city.append(list(map(int, input().split())))
plan = list(map(int, input().split()))


def bfs(start,next):
    que =deque()
    que.append(start)
    visited = [0 for _ in range(n)]
    while que:
        start = que.popleft()
        visited[start] = 1
        if start == next:
            return True
        else:
            for i in range(n):
                if city[start][i] == 1:
                    if visited[i] == 0:
                        que.append(i)
                        visited[i] = 1
    else:
        return False

check = True
for i in range(m-1):
    if plan[i] != plan[i+1]:
        check = bfs(plan[i]-1, plan[i+1]-1)
        if check == False:
            print("NO")
            break
if check == True:
    print("YES")