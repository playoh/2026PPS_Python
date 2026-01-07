doorNum = int(input())
wayNum = int(input())

# print("num :",num)
past = 0
current = wayNum
tmp = wayNum

# print(current, wayNum, past)
count = 1
while(count != doorNum):
    if (tmp == 1):
        tmp = 0
        current = tmp
        past = 1
    elif (tmp == 0):
        tmp = 1
        current = tmp
        past = 0
    print(current)
    count += 1




