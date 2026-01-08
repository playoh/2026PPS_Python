doorNum = int(input())
wayNum = int(input())

# print("num :",num)
past = 0
current = wayNum
tmp = wayNum


for i in range(2,doorNum+1):
    if (tmp == 1):
        tmp = 0
        current = tmp
        past = 1
    elif (tmp == 0):
        tmp = 1
        current = tmp
        past = 0
    if(i %3 == 0 and current != wayNum):
        print("Love is open door")
        exit()

current = wayNum
tmp = wayNum

for _ in range(2, doorNum+1):
    if(tmp == 1):
        tmp = 0
        current = tmp
    else:
        tmp = 1
        current = tmp

    print(current)





