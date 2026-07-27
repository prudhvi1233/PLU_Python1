import sqlite3
from collections import deque

conn = sqlite3.connect("cab.db")
cur = conn.cursor()

cur.execute("""
SELECT drivers.id, drivers.name, bookings.area
FROM drivers
JOIN bookings ON drivers.id = bookings.driver_id
WHERE drivers.available = 1
""")

rows = cur.fetchall()
graph = {}

for row in rows:
    driver = row[1]
    area = row[2]

    if driver not in graph:
        graph[driver] = []

    graph[driver].append(area)

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

print("Nearest Available Driver")

for start in graph:
    bfs(graph, start)
    nearest = start
    break


print("\nAssigned Driver:", nearest)

cur.execute("UPDATE drivers SET available=0 WHERE name=?", (nearest,))
conn.commit()

print("Driver Availability Updated")

conn.close()