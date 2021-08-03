#좌표 수
n = int(input())
x_list = []
y_list = []
for i in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    x_list.append(a)
    y_list.append(b)

x_list.append(x_list[0])
y_list.append(y_list[0])
suma = 0
sumb = 0

for i in range(len(x_list)-1):
    suma += x_list[i]*y_list[i+1]

for j in range(len(y_list)-1):
    sumb += y_list[j]*x_list[j+1]

sum = (sumb - suma)/2
#절대값으로 출력하며 소수2째자리에서 반올림
print(abs(round(sum,2)))