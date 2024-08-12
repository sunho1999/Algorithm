# n,m = map(int,input().split())
#
# answer = 0
# book_list = list(map(int,input().split()))
# srt_list = sorted(book_list,key = lambda x:abs(x))
# srt_list = srt_list[::-1]
# plus_list = []
# minus_list = []
# for i in book_list:
#     if i > 0:
#         plus_list.append(i)
#     else:
#         minus_list.append(i)
# plus_list.sort(reverse=True)
# minus_list.sort()
# #
# if srt_list[0] > 0: # 제일 먼 곳이 양수 일 때
#     for i in range(0,len(minus_list),m):
#         answer = answer + abs((minus_list[i]))*2
#     plus_list = plus_list[::-1]
#     # print(answer)
#     if len(plus_list) <= m:
#         answer = answer + abs(plus_list[-1])
#     else:
#         for i in range(0,len(plus_list),m):
#             if i == len(plus_list)-1:
#                 answer = answer + abs(plus_list[i])
#             else:
#                 answer = answer + (abs(plus_list[i]))*2
#
# elif srt_list[0] < 0: # 제일 먼곳이 음수 일 때
#     for i in range(0,len(plus_list),m):
#         answer = answer + (plus_list[i])*2
#     minus_list = minus_list[::-1]
#     if len(minus_list) <= m:
#         answer = answer + abs(minus_list[-1])
#     else:
#         for i in range(0,len(minus_list),m):
#             if i == len(minus_list)-1:
#                 answer = answer + abs(minus_list[i])
#             else:
#                 answer = answer + (abs(minus_list[i]))*2
# print(answer)
n, m = map(int, input().split())
book_list = list(map(int, input().split()))

# 절대값 기준으로 내림차순 정렬
book_list.sort(key=lambda x: abs(x), reverse=True)

# 양수, 음수 분리
plus_list = [x for x in book_list if x > 0]
minus_list = [x for x in book_list if x < 0]

answer = 0

# 절대값이 가장 큰 값을 마지막에 방문하도록 한다
if plus_list and (not minus_list or abs(plus_list[0]) >= abs(minus_list[0])):
    answer += abs(plus_list[0])  # 제일 먼 양수 위치를 한번만 방문
    plus_list = plus_list[m:]  # 한 번 방문했으므로 M권 제거
else:
    answer += abs(minus_list[0])  # 제일 먼 음수 위치를 한번만 방문
    minus_list = minus_list[m:]  # 한 번 방문했으므로 M권 제거

# 나머지 책들은 왕복
for i in range(0, len(plus_list), m):
    answer += 2 * abs(plus_list[i])
for i in range(0, len(minus_list), m):
    answer += 2 * abs(minus_list[i])

print(answer)
