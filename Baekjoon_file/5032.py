e, f, c = map(int, input().split())
#그날 가지고 있는 병의수 e
#빈병 수 f
#바꾸는 병의수 c

n = (e+f)//c + (e+f)%c
res = (e+f)//c
while n//c:
    res += n//c
    n = n//c + n%c
print(res)