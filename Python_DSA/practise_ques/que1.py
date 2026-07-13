# Question 2 : 
'''
A social media platform stores friendships between users.

Requirements
    Create a graph where each user is connected to their friends.
    Display all users and their friends in a formated way.
    Store all usernames in a list.
    Sort the usernames using Insertion Sort.
    Ask the user to enter a name to see if they exists (binary search) and if they are connected.
    If found, display all of the user's friends.
'''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


graph = {}

n = int(input("Enter number of users: "))

for _ in range(n):
    user = input("Enter username: ")
    graph[user] = []

for user in graph:
    count = int(input(f"Enter number of friends of {user}: "))
    for _ in range(count):
        friend = input("Friend: ")
        graph[user].append(friend)

print("\nUsers and their friends:")
for user in graph:
    print(f"{user} -> {', '.join(graph[user])}")

usernames = list(graph.keys())
insertion_sort(usernames)

print("\nSorted usernames:")
for name in usernames:
    print(name)

search = input("\nEnter username to search: ")

index = binary_search(usernames, search)

if index != -1:
    print("\nUser found!")
    print(f"Friends of {search}:")
    if graph[search]:
        for friend in graph[search]:
            print(friend)
    else:
        print("No friends.")
else:
    print("User not found.")