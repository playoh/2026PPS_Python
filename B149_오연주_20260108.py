import sys
from itertools import repeat

count, length = map(int, input().split())
word = ["" for _ in range(count)]
seen = {}

for i in range(count):
    w = sys.stdin.readline().strip()
    if(len(w)>=length):
        seen[w] = seen.get(w,0) + 1

for key, val in sorted(seen.items(),key=lambda x:(-x[1], -len(x[0]), x[0])):
    print(key)