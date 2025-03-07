import sys
sys.setrecursionlimit(10**9)
def dfs(start):
    global answer
    cycle.append(start)
    check_num_list[start] = True
    next_node = student_list[start]

    if check_num_list[next_node]:  # 방문 가능 체크
        if next_node in cycle:  # 사이클 가능
            answer += cycle[cycle.index(next_node):]  # 사이클 구간 팀 이룸
        return
    else:
        dfs(next_node)
testcase = int(input())

for i in range(testcase):
    answer = []
    student_num = int(input())
    student_list = [0] + list(map(int,input().split()))
    check_num_list = [True] + [False for _ in range(student_num)]
    for i in range(1,student_num+1):
        cycle = []
        dfs(i)
    print(student_num - len(list(set(answer))))