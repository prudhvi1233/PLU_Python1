'''
5. Insert New Book by Price
A bookstore maintains a sorted list of book prices.
A new book arrives, and its price needs to be placed at the correct
position while keeping the list sorted.
Write a program to perform this task.
'''
n = int(input())

prices = []

for i in range(n):
    prices.append(int(input()))

new_price = int(input())

prices.append(0)

i = n - 1

while i >= 0 and prices[i] > new_price:
    prices[i + 1] = prices[i]
    i -= 1

prices[i + 1] = new_price

for i in range(n + 1):
    print(prices[i], end=" ")