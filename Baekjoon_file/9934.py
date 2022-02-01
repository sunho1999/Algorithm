n = int(input())

num_list = list(map(int,input().split()))
answer = [[] for i in range(n)]

def binary(list,cnt):
    if cnt == n+1:
        return answer
    else:
        if len(list) % 2 == 1: #길이가 홀수 일때
            answer[cnt-1].append(list[len(list)//2])
            left_list = list[0:len(list)//2]
            right_list = list[len(list)//2+1:]
            cnt +=1
            binary(left_list,cnt)
            binary(right_list,cnt)
binary(num_list,1)

for i in answer:
    for j in i:
        print(j,end = " ")
    print()