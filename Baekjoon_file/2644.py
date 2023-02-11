from collections import deque
n = int(input())
first_num , second_num = map(int,input().split())
if first_num > second_num:
    a = first_num
    first_num = second_num
    second_num = a
m = int(input())
list1 = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    list1[a].append(b)
    list1[b].append(a)
que = deque()
visited = [0 for _ in range(n+1)]
que.append([first_num,0])
i = first_num

while(que):
    num,cnt = que.popleft()
    visited[num] = 1
    if num == second_num:
        print(cnt)
        exit()
    cnt += 1
    for i in list1[num]:
        if visited[i] == 0:
            que.append([i,cnt])
if num != second_num:
    print(-1)