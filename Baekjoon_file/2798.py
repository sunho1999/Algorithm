a,b = input().split()
a = int(a)
b = int(b)
card_list = list(map(int,input().split()))
sum =[]

for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            if card_list[i]+card_list[j]+card_list[k] <= b:
                sum.append(card_list[i]+card_list[j]+card_list[k])
                continue
print(max(sum))
