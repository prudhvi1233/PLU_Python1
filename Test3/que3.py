'''
3. Arrange Exam Marks
A teacher wants to display students' marks from the lowest to the
highest.
Write a program to sort the marks of all students in ascending order
'''
n = int(input())

marks = []

for i in range(n):
    marks.append(int(input()))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]

for i in range(n):
    print(marks[i], end=" ")