testcase = int(input())

for i in range(testcase):
    edge_num = int(input())
    cnt = 0
    for i in range(edge_num):
        freind_list = [[] for _ in range(edge_num)]
        dic = {}
        a_friend, b_friend = input().split()
        print(a_friend,b_friend).
        if not freind_list : # 친구가 처음에 비어있을 때
            freind_list[cnt].append(a_friend)
            cnt +=1
            freind_list[cnt].append(b_friend)
        else:
