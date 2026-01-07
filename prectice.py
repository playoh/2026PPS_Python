board = []

for _ in range(10):
    row = list(map(int, input().split()))
    board.append(row)

x, y = 1,1

while True:
    if(board[x][y] == 0):
        board[x][y] = 9
    elif(board[x][y] == 2):
        board[x][y] = 9
        break

    if(board[x][y+1] != 1):
        y+=1
    elif(board[x+1][y] != 1):
        x+=1
    else:
        break


for i in range(10):
    print(*board[i])