test_case = int(input())

for i in range(test_case):
    a_cnt = 0
    b_cnt = 0
    answer = "NO"
    a = input()
    for j in a:
        if j =="(":
            a_cnt+=1
        elif j == ")":
            b_cnt+=1
            if b_cnt > a_cnt:
                answer = "NO"
                break
    if (b_cnt == a_cnt) and (a_cnt>=1):
                answer = "YES"
    else:
        answer = "NO"

    print(answer)