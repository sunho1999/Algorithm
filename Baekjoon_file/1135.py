n = int(input()) # 회사 직원수

tree = [[] for _ in range(n)] # tree
input_list = list(map(int,input().split()))
child_cnt = [0 for _ in range(n)]

def find_child(parent):
    global child_cnt
    print(child_cnt)
    child_node = [] # child 개수 담을 변수
    if tree[parent] == []: # 만약 자식 노드가 없다 -> 0 으로 초기화
        child_cnt[parent] = 0
    else:
        for child in tree[parent]: # 자식노드 탐색
            find_child(child)
            child_node.append(child_cnt[child])

        child_node.sort(reverse=True)
        child_node = [child_node[i] + i + 1 for i in range(len(child_node))]
        child_cnt[parent] = max(child_node)


for i in range(1,len(input_list)):
    tree[input_list[i]].append(i) # node 추가



find_child(0)
print(child_cnt)