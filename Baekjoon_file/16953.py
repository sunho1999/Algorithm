from collections import deque

start_num ,target_num = map(int,input().split())

num_dict = {}
que = deque()
first_num = start_num * 2
second_num = int(str(start_num)+"1")
cnt = 1
que.append((start_num,cnt))

while que:
    number, cn = que.popleft()
    # print(number)
    if number > target_num: # 만약 뽑은 숫자가 이미 타겟넘버를 지나갔으면
        pass
    else:
        first_num = number * 2
        second_num = int(str(number) + "1")

        if first_num == target_num or second_num == target_num: # target number랑 같으면
            print(cn+1)
            break
        elif first_num < target_num or second_num < target_num: # 숫자가 작을 때
            if first_num not in num_dict:
                tn = cn + 1
                num_dict[first_num] = tn
                que.append((first_num,tn))

            elif first_num in num_dict:
                tn = cn + 1
                if num_dict[first_num] > tn:
                    num_dict[first_num] = tn

            if second_num not in num_dict:
                kn = cn + 1
                num_dict[second_num] = kn
                que.append((second_num, kn))
            elif second_num in num_dict:
                tn = cn + 1
                if num_dict[second_num] > tn:
                    num_dict[second_num] = tn
        else: # 숫자가 클 때
            if len(que) > 0:
                continue
else:
    print(-1)


# print(num_dict)
