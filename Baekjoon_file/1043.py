import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
#아는사람
liers = deque(map(int, input().split()))
liers.popleft()
group = []
for i in range(m):
    group.append(list(map(int, input().split())))

# 각 그룹 확인
lierState = []
for i in range(m):
    lierState.append([])

ans = 0
alreadyLied = []
#라이어 큐 빌때까지 탐색
while liers:
    curLier = liers.popleft()
    alreadyLied.append(curLier)
    for i in range(m):
        #라이어가 있으면 그 방 인덱스 추가
        if curLier in group[i][1:]:
            lierState[i].append(True)
            for j in range(len(group[i]) - 1):
                #그 방에 있는 사람들 전부다 추가
                curPerson = group[i][j + 1]
                if (not curPerson in alreadyLied) and (not curPerson in liers):
                    liers.append(curPerson)
        else:
            lierState[i].append(False)

for i in range(m):
    if True in lierState[i]:
        continue
    else:
        ans += 1

print(ans)