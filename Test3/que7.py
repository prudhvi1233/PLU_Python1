'''
7. Online Game Leaderboard
An online gaming platform stores players' scores.
Write a program to arrange the scores in descending order so that the
leaderboard can be displayed.
'''
n = int(input())

scores = []

for i in range(n):
    scores.append(int(input()))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if scores[j] < scores[j + 1]:
            scores[j], scores[j + 1] = scores[j + 1], scores[j]

for i in range(n):
    print(scores[i], end=" ")