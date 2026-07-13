'''8. Hospital Emergency Queue
A hospital has a list of patients with different priority levels.
Write a program to arrange the patients so that the patient with the
highest priority is treated first.'''

n = int(input())

priority = []

for i in range(n):
    priority.append(int(input()))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if priority[j] < priority[j + 1]:
            priority[j], priority[j + 1] = priority[j + 1], priority[j]

for i in range(n):
    print(priority[i], end=" ")


