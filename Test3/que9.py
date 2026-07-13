'''
9. Library Book Search
A library has 10,000 books, and the Book IDs are already arranged in
ascending order.
Write a program to find a given Book ID efficiently.
Also mention which searching algorithm you used and why it is suitable.
'''

n = int(input())

book_ids = []

for i in range(n):
    book_ids.append(int(input()))

key = int(input())

low = 0
high = n - 1

found = False

while low <= high:
    mid = (low + high) // 2

    if book_ids[mid] == key:
        print("Book ID found at index", mid)
        found = True
        break
    elif book_ids[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Book ID not found")