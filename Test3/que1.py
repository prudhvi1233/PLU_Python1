'''
1. Student Roll Number Search
A teacher has stored the roll numbers of students in a list in the order
they registered. The list is not sorted.
Write a program to check whether a given roll number exists in the list.
If found, display its position; otherwise, print "Student Not Found."
'''

rolls = list(map(int, input().split()))
key = int(input())

for i, roll in enumerate(rolls):
    if roll == key:
        print(i)
        break
else:
    print("Student Not Found")