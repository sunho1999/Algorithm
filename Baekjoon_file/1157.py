x = input().upper()
x_list = list(set(x))
cnt = []

for i in x_list:
    count = x.count(i)
    cnt.append(count)

if cnt.count(max(cnt))>=2:
    print("?")
else:
    print(x_list[(cnt.index(max(cnt)))])
