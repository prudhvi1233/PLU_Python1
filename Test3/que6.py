'''
6. Employee Salary Report
An HR department has employee salary records collected from two different
branches.
Write a program to combine both lists and display all salaries in
ascending order.
'''
n1 = int(input())

salary1 = []

for i in range(n1):
    salary1.append(int(input()))

n2 = int(input())

salary2 = []

for i in range(n2):
    salary2.append(int(input()))

salary = salary1 + salary2

n = len(salary)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if salary[j] > salary[j + 1]:
            salary[j], salary[j + 1] = salary[j + 1], salary[j]

for i in range(n):
    print(salary[i], end=" ")