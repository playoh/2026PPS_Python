n = int(input())
answer = 0

for i in range(n):
    c = input()
    past = c[0]
    seen = []
    is_group = True

    count = 0

    for j in range(1, len(c)):
        if c[j] != past:
            if c[j] in seen:
                is_group = False
                break
            seen.append(past)
            past = c[j]

    if is_group:
        answer += 1

print(answer)
