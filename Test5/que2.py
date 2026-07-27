import sqlite3

class Product:
    def __init__(self, pid, name, category, qty, price):
        self.pid = pid
        self.name = name
        self.category = category
        self.qty = qty
        self.price = price

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i].qty < right[j].qty:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid].pid == key:
            return mid
        elif arr[mid].pid < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

conn = sqlite3.connect("inventory.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS products(pid INTEGER PRIMARY KEY,name TEXT,category TEXT,qty INTEGER,price REAL)")

cur.execute("SELECT * FROM products")
rows = cur.fetchall()

products = []

for row in rows:
    products.append(Product(*row))

merge_sort(products)

print("Products Sorted by Quantity")
for p in products:
    print(p.pid, p.name, p.category, p.qty, p.price)

products.sort(key=lambda x: x.pid)

pid = int(input("Enter Product ID: "))
index = binary_search(products, pid)

if index != -1:
    p = products[index]
    print("Found:", p.pid, p.name, p.category, p.qty, p.price)
else:
    print("Product Not Found")

print("\nStock Below 10")
for p in products:
    if p.qty < 10:
        print(p.pid, p.name, p.qty)

conn.close()