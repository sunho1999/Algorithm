n = int(input())

lope_list = []
for i in range(n):
    lope_list.append(int(input()))

lope_list.sort(reverse=True)
answer = 0
for i in range(n) :
    tmp = lope_list[i]
    if(answer < (i+1) * tmp) :
        answer = (i+1) *tmp


print(answer)