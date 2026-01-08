from itertools import repeat

count, length = map(int, input().split())
word = ["" for _ in range(count)]

for i in range(count):
    word[i] = input()

seen = {}

for w in word:
    if len(w) >= length:
        if w in seen:
            seen[w] += 1
        else:
            seen[w] = 1

for key, val in sorted(seen.items(),key=lambda x:(-x[1], -len(x[0]), x[0])):
    print(key)