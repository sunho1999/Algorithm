#  구역을 두 개의 선거구로 나눠야 하고, 각 구역은 두 선거구 중 하나에 포함되어야 한다.
#  선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다.
#  구역 A에서 인접한 구역을 통해서 구역 B로 갈 수 있을 때, 두 구역은 연결되어 있다고 한다.
#  중간에 통하는 인접한 구역은 0개 이상이어야 하고, 모두 같은 선거구에 포함된 구역이어야 한다.
import itertools
import collections
import sys
input = sys.stdin.readline

def bfs(same):
    start = same[0] # 조합된 노드 중 첫번째 노드로 start지점 생성
    # print(start)
    q = collections.deque([start]) # deque로 탐색 노드 값 저장
    visited = set([start])
    # print(visited)
    _sum = 0
    while q:
        v = q.popleft() # 처음 노드 값 추출
        _sum += node_number[v] # 해당 노드의 인구수 값 저장
        # print(linked_list[v])
        for u in linked_list[v]: # 탐색할 노드의 인접 노드 탐색
            if u not in visited and u in same: # 인접 노드가 방문하지 않은 노드이며 조합된 노드들로 구성된 경우,
                q.append(u) # q에 추가
                visited.add(u) # 방문한 노드로 체크
    return _sum, len(visited) # 탐색 한 노드들의 인구수 합, 노드 길이 리턴


n = int(input())
node_number = list(map(int,input().split()))
# print(node_number)
result = float('inf')
linked_list = [[] for _ in range(n)]

for i in range(n):
    near_node = list(map(int,input().split()))
    for j in range(1, near_node[0] + 1):
        linked_list[i].append(near_node[j] - 1)

    # linked list형태로 인접 노드 저장
# print(linked_list)
for i in range(1, n//2 + 1):
    combis = list(itertools.combinations(range(n), i)) # 주어진 노드로 조합 생성
    for combi in combis: # 조합 탐색
        # print(combi)
        sum1, v1 = bfs(combi) # 조합 된 노드 탐색 시작
        sum2, v2 = bfs([i for i in range(n) if i not in combi]) # 그외 조합되지 않은 노트 탐색 시작
        if v1 + v2 == n:  # 2번의 bfs를 통해 모든 노드가 방문되었는지 확인한다.
            result = min(result, abs(sum1 - sum2))

if result != float('inf'):
    print(result)
else:
    print(-1)
