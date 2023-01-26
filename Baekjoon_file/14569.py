total_subject = int(input())
each_subject = []
for _ in range(total_subject):
    subject = list(map(int,input().split()))
    each_subject.append(set(subject[1:]))

total_student = int(input())
each_student = []
for _ in range(total_student):
    student = list(map(int,input().split()))
    each_student.append(set(student[1:]))

for i in range(len(each_student)):
    cnt = 0
    for j in range(len(each_subject)):
        if each_subject[j].intersection(each_student[i]) == each_subject[j]: #교집합을 구했을 때 subject와 같다면 cnt +1씩 증가
            cnt +=1
    print(cnt)