bin_list = [64,32,16,8,4,2,1]

n = int(input())
cnt = 0

for i in bin_list:
    if n in bin_list:
        cnt +=1
        break
    else:
        if i > n:
            continue
        else:
            n = n % i # 몫
            cnt +=1
print(cnt)