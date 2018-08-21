'''
nestedlists.py
Nested Lists HackerRank Challenge In Python



'''

# number of students
N = int(raw_input())
# create a list that will have grades
final = list()
for i in range(N):
    lst = list()
    name = str(raw_input())
    marks = float(raw_input())
    # add name and mark the student received
    lst.append(name)
    lst.append(marks)
    final.append(lst)

# print final
# print len(final)
k = list()
for i in range(len(final)):
    k.append(final[i][1])
# print k
x = min(k)
k1 = list()
for i in range(len(k)):
    if x != k[i]:
        k1.append(k[i])
y = min(k1)
# print x
student = list()
for i in range(len(final)):
    if y == final[i][1]:
        student.append(final[i][0])
student.sort()
for i in range(len(student)):
    print student[i]
