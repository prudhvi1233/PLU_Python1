import sqlite3

class Movie:
    def __init__(self, mid, title, genre, rating, watch):
        self.mid = mid
        self.title = title
        self.genre = genre
        self.rating = rating
        self.watch = watch

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid].mid == key:
            return mid
        elif arr[mid].mid < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

conn = sqlite3.connect("movies.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS movies(
mid INTEGER PRIMARY KEY,
title TEXT,
genre TEXT,
rating REAL,
watch INTEGER)
""")

cur.execute("SELECT * FROM movies")
rows = cur.fetchall()

movies = []

for row in rows:
    movies.append(Movie(*row))

movies.sort(key=lambda x: x.rating, reverse=True)

print("Movies Sorted by Rating")

for m in movies:
    print(m.mid, m.title, m.genre, m.rating, m.watch)

movies.sort(key=lambda x: x.mid)

mid = int(input("Enter Movie ID: "))

index = binary_search(movies, mid)

if index != -1:
    m = movies[index]
    print("Found:", m.mid, m.title, m.genre, m.rating, m.watch)
else:
    print("Movie Not Found")

movies.sort(key=lambda x: x.rating, reverse=True)

print("\nTop 10 Highest Rated Movies")

for m in movies[:10]:
    print(m.mid, m.title, m.rating)

print("\nMost Watched Movie in Every Genre")

cur.execute("""
SELECT genre, title, MAX(watch)
FROM movies
GROUP BY genre
""")

for row in cur.fetchall():
    print(row)

conn.close()