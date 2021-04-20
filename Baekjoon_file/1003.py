
def fibo(num):
    aa = len(zero_cnt)
    if num >= aa:
    #2까지 수는 그냥 통과
        for i in range(aa,num+1):
            zero_cnt.append(zero_cnt[i-1]+zero_cnt[i-2])
            one_cnt.append(one_cnt[i-1]+one_cnt[i-2])
    print("%d %d"%(zero_cnt[num],one_cnt[num]))

n = int(input())
zero_cnt = [1,0,1]
one_cnt = [0,1,1]
for i in range(n):
    a = int(input())
    fibo(a)