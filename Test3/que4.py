'''
4. Rank Participants
A sports academy has recorded the timings (in seconds) of participants in
a race.
Write a program to arrange the timings from the fastest to the slowest so
that the winners can be announced.
'''

n = int(input())

timings = []

for i in range(n):
    timings.append(int(input()))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if timings[j] > timings[j + 1]:
            timings[j], timings[j + 1] = timings[j + 1], timings[j]

for i in range(n):
    print(timings[i], end=" ")