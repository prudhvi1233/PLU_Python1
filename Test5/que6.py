import sqlite3
from collections import deque

conn = sqlite3.connect("food.db")
cur = conn.cursor()

cur.execute("""
SELECT orders.id, restaurant.name, delivery.area
FROM orders
JOIN restaurant ON orders.rid = restaurant.id
JOIN delivery ON orders.did = delivery.id
WHERE orders.status='Pending'
""")

orders = cur.fetchall()

graph = {}

for order in orders:
    restaurant = order[1]
    area = order[2]

    if restaurant not in graph:
        graph[restaurant] = []

    graph[restaurant].append(area)

def bfs(graph, start):
    visited = set()
    q = deque([start])

    while q:
        node = q.popleft()

        if node not in visited:
            visited.add(node)
            print(node)

            for i in graph.get(node, []):
                if i not in visited:
                    q.append(i)

print("Delivery Order")

for start in graph:
    bfs(graph, start)
    break

for order in orders:
    cur.execute("UPDATE orders SET status='Completed' WHERE id=?", (order[0],))

conn.commit()

print("\nCompleted Deliveries Updated")

conn.close()