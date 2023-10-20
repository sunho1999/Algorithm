import sys

input = sys.stdin.readline

s = input().strip()
# print(s)
list1 = []
answer = 0

for i in s:
    if i == ")":
        t = 0
        while len(list1) != 0:
            top = list1.pop()
            if top == "(":
                if t == 0:
                    list1.append(2)
                else:
                    list1.append(2 * t)
                break
            elif top == "[":
                print(0)
                exit(0)
            else:
                t = t + int(top)
    elif i == "]":
        t = 0
        while len(list1 ) != 0:
            top = list1 .pop()
            if top == "[":
                if t == 0:
                    list1 .append(3)
                else:
                    list1 .append(3 * t)
                break
            elif top == "(":
                print(0)
                exit(0)
            else:
                t = t + int(top)
    else:
        list1.append(i)

for i in list1 :
    if i == "(" or i == "[":
        print(0)
        exit(0)
    else:
        answer += i

print(answer)