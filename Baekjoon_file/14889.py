import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

# def bfs(list1):
    # start_node = list1[0]
    # que = deque()
    # que.append(start_node)
    # visited = []
    # visited.append(start_node)
    # sum1 = 0
    # while que:
    #     node = que.popleft()

n = int(input().strip())
matirx = []
for i in range(n):
    matirx.append(list(map(int,input().split())))
min_value = float('inf')
for combi in combinations(range(n),n//2):
    answer1= 0
    answer2 = 0
    combi = (list(combi)) # 조합 된 노드 탐색 시작
    another_combi = [i for i in range(n) if i not in combi] # 그외 조합되지 않은 노트 탐색 시작
    for r in combinations(combi, 2):  # 5
        answer1 += matirx[r[0]][r[1]]
        answer1 += matirx[r[1]][r[0]]
    for r in combinations(another_combi, 2):  # 6
        answer2 += matirx[r[0]][r[1]]
        answer2 += matirx[r[1]][r[0]]
    min_value = min(min_value, abs(answer1 - answer2))  # 7
print(min_value)
