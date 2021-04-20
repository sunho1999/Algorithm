while(True):
    try:
        a = list(map(int,input().split()))
        sum =0
        for i in a:
            sum +=i
        print(sum)
    except:
        break