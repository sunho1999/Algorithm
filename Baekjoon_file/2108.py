import sys
from collections import Counter

n = int(input())
n_number = []
for i in range(n):
    number = int(sys.stdin.readline())
    n_number.append(number)

n_number.sort()

print(round(sum(n_number) / len(n_number)))
medain = n_number[len(n_number)//2] #  중앙값
print(int(medain))
mode = Counter(n_number).most_common()
mode_value = 0
if len(mode) == 1:
    mode_value = mode[0][0]
elif mode[0][1] == mode[1][1]:
    mode_value = mode[1][0]
else:
    mode_value = mode[0][0]
print(mode_value)
print(abs(max(n_number) - min(n_number)))


