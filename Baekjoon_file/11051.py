test_case = int(input())

for i in range(test_case):
    sum1 = 0
    cnt = int(input())
    price_list = list(map(int,input().split()))
    purchase_cnt = []
    max_num = 0
    for i in range(len(price_list)-1,-1,-1):
        # print(price_list[i])
        if price_list[i] > max_num:
            max_num = price_list[i]
        else:
            sum1 += max_num-price_list[i]
    print(sum1)
