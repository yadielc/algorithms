'''
nestedlists.py
Nested Lists HackerRank Challenge In Python

The task is to write a program that displays the second
lowest grades that the students received, given a set of students
However, more than 1 student can receive the second lowest grades.
Thus, the output must be a sorted list of the names of the students
that received the second lowest grade.

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
    # add to separate list
    final.append(lst)

# print final list
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

# print x, the sorted list with the names of the students that obtained the second lowest grade 
student = list()
for i in range(len(final)):
    if y == final[i][1]:
        student.append(final[i][0])
student.sort()
for i in range(len(student)):
    print student[i]
