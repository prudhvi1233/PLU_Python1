'''10. School Annual Report
A school has recorded the marks of 50 students.
Write a program that:
Sorts the marks in ascending order.
Accepts a mark from the user.
Checks whether that mark exists in the sorted list.
Displays the position if found; otherwise, prints "Mark Not Found."'''

n = int(input())
marks = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(n - i - 1):
        if marks[j] > marks[j + 1]:
            temp = marks[j]
            marks[j] = marks[j + 1]
            marks[j + 1] = temp

print(*marks)

key = int(input())

found = False

for i in range(n):
    if marks[i] == key:
        print(i)
        found = True
        break

if not found:
    print("Mark Not Found")