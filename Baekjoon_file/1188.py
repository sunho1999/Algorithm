n,m = map(int,input().split())
check = 0
if n % m == 0:
    print(0)
else:
    for i in range(1,101):
        if i > m and i > n:
            break
        else:
            if m % i == 0 and n % i == 0:
                check = i
    print(m-check)