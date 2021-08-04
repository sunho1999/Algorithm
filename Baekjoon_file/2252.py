from collections import deque
import  sys

#n 학생수, m은 규칙수
n,m = map(int,sys.stdin.readline().split())
#학생 indegree 담을 리스트
student = [0 for _ in range(n+1)]
matrix = [[] for _ in range(n+1)]

que = deque()

for i in range(m):
    # 우선순위가 늦을수록 indegree +=1
    first,second = map(int,sys.stdin.readline().split())
    matrix[first].append(second)
    student[second] += 1
# indegree 0인 학생들 추출
for i in range(1,n+1):
    if student[i] == 0:
        que.append(i)

while que:
    a = que.popleft()
    for i in matrix[a]:
        student[i] -= 1
        if student[i] == 0:
            que.append(i)
    print(a, end = ' ')
