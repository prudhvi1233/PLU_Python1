import sqlite3

class Transaction:
    def __init__(self, tid, acc, amount, date, ttype):
        self.tid = tid
        self.acc = acc
        self.amount = amount
        self.date = date
        self.ttype = ttype

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

def partition(arr, low, high):
    pivot = arr[high].amount
    i = low - 1

    for j in range(low, high):
        if arr[j].amount <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid].tid == key:
            return mid
        elif arr[mid].tid < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

conn = sqlite3.connect("bank.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS transactions(
tid INTEGER PRIMARY KEY,
accno TEXT,
amount REAL,
date TEXT,
type TEXT)""")

cur.execute("SELECT * FROM transactions")
rows = cur.fetchall()

transactions = []

for row in rows:
    transactions.append(Transaction(*row))

if len(transactions) > 0:
    quick_sort(transactions, 0, len(transactions) - 1)

print("Transactions Sorted by Amount")
for t in transactions:
    print(t.tid, t.acc, t.amount, t.date, t.ttype)

transactions.sort(key=lambda x: x.tid)

tid = int(input("Enter Transaction ID: "))
index = binary_search(transactions, tid)

if index != -1:
    t = transactions[index]
    print("Found:", t.tid, t.acc, t.amount, t.date, t.ttype)
else:
    print("Transaction Not Found")

credit = 0
debit = 0

for t in transactions:
    if t.ttype.lower() == "credit":
        credit += t.amount
    else:
        debit += t.amount

print("Total Credit =", credit)
print("Total Debit =", debit)

transactions.sort(key=lambda x: x.amount, reverse=True)

print("\nTop 5 Highest Transactions")
for t in transactions[:5]:
    print(t.tid, t.acc, t.amount)

conn.close()