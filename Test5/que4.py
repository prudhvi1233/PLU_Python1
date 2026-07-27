import sqlite3

class Student:
    def __init__(self, roll, name, cgpa, skills, status):
        self.roll = roll
        self.name = name
        self.cgpa = cgpa
        self.skills = skills
        self.status = status

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left].cgpa > arr[largest].cgpa:
        largest = left

    if right < n and arr[right].cgpa > arr[largest].cgpa:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def binary_search(arr, key):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high)//2

        if arr[mid].roll == key:
            return mid
        elif arr[mid].roll < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

conn = sqlite3.connect("college.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
roll INTEGER PRIMARY KEY,
name TEXT,
cgpa REAL,
skills TEXT,
status TEXT)
""")

cur.execute("SELECT * FROM students")
rows = cur.fetchall()

students = []

for row in rows:
    students.append(Student(*row))

heap_sort(students)

print("Students Sorted by CGPA")

for s in students:
    print(s.roll, s.name, s.cgpa, s.skills, s.status)

students.sort(key=lambda x: x.roll)

roll = int(input("Enter Roll Number: "))

index = binary_search(students, roll)

if index != -1:
    s = students[index]
    print("Found:", s.roll, s.name, s.cgpa, s.skills, s.status)
else:
    print("Student Not Found")

print("\nEligible Students (CGPA > 7.5)")

for s in students:
    if s.cgpa > 7.5:
        print(s.roll, s.name, s.cgpa)

roll = int(input("\nEnter Selected Student Roll Number: "))

cur.execute("UPDATE students SET status='Placed' WHERE roll=?", (roll,))
conn.commit()

print("Placement Status Updated")

conn.close()