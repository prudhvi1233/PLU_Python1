'''
2. Product ID Search
An e-commerce website stores product IDs in ascending order.
Write a program to find whether a customer-entered product ID exists in
the inventory. If it exists, display its index; otherwise, display "Product
Not Available."
'''
products = list(map(int, input().split()))
key = int(input())

low = 0
high = len(products) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if products[mid] == key:
        print(mid)
        found = True
        break
    elif products[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Product Not Available")