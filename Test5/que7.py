import sqlite3
from datetime import datetime

class Employee:
    def __init__(self, eid, name, checkin, checkout):
        self.eid = eid
        self.name = name
        self.checkin = checkin
        self.checkout = checkout

        t1 = datetime.strptime(checkin, "%H:%M")
        t2 = datetime.strptime(checkout, "%H:%M")

        self.hours = (t2 - t1).seconds / 3600

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid].eid == key:
            return mid
        elif arr[mid].eid < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

conn = sqlite3.connect("attendance.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS attendance(
eid INTEGER PRIMARY KEY,
name TEXT,
checkin TEXT,
checkout TEXT)
""")

cur.execute("SELECT * FROM attendance")
rows = cur.fetchall()

employees = []

for row in rows:
    employees.append(Employee(*row))
employees.sort(key=lambda x: x.hours, reverse=True)

print("Employees Sorted by Working Hours")

for e in employees:
    print(e.eid, e.name, e.hours)
employees.sort(key=lambda x: x.eid)

eid = int(input("Enter Employee ID: "))

index = binary_search(employees, eid)

if index != -1:
    e = employees[index]
    print("Found:", e.eid, e.name, e.hours)
else:
    print("Employee Not Found")

print("\nEmployees Worked More Than 45 Hours")

for e in employees:
    if e.hours > 45:
        print(e.eid, e.name, e.hours)

conn.close()