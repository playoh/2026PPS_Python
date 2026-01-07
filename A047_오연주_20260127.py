s = input()

result = [s[i:i+10] for i in range(0, len(s), 10)]

for i in range(len(result)):
    print(result[i])
