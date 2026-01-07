doorNum = int(input("Enter the Door number: "))
print("Way to open the Door: 0 is push and 1 is pull \n")
wayNum = int(input("Enter the way to open the door: "))

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



