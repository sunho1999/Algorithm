from collections import deque

def bfs(start_num,depth):
    global answer
    que = deque()
    que.append((start_num,depth))
    while que:
        start_num,depth = que.popleft()
        visited_list[start_num] = True
        for i in linked_list[start_num]:
            if visited_list[i] != True and depth < 2:
                visited_list[i] = True
                que.append((i,depth+1))
                answer +=1


number = int(input())
linked_list = [[] for _ in range(number+1)]
visited_list = [False for _ in range(number+1)]
testcase = int(input())

answer = 0
for i in range(testcase):
    n,m = map(int,input().split())
    linked_list[n].append(m)
    linked_list[m].append(n)

bfs(1,0)
print(answer)