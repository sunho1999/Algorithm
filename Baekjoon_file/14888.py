n = int(input())
number_list = list(map(int,input().split()))
operator_list = list(map(int,input().split())) #덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.
min_num = 1e9
max_num = -1e9
def operator(depth, total,plus,minus,multi,div):
    global min_num
    global max_num
    # print(depth, max_num,min_num)
    if depth == n:
        max_num = max(total, max_num)
        min_num = min(total, min_num)
        return
    if plus:
        operator(depth + 1,total + number_list[depth],plus-1,minus,multi,div)
    if minus:
        operator(depth + 1, total - number_list[depth], plus, minus - 1, multi, div)
    if multi:
        operator(depth + 1, total * number_list[depth], plus, minus, multi - 1, div)
    if div:
        operator(depth + 1, int(total / number_list[depth]), plus, minus, multi, div - 1)


operator(1,number_list[0],operator_list[0],operator_list[1],operator_list[2],operator_list[3])
print(int(max_num))
print(int(min_num))
# print((-3//5))