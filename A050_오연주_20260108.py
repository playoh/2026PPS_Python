letter = input()

for i in range (len(letter)):
    match letter[i]:
        case 'A':
            print('X',end='')
        case 'B':
            print('Y',end='')
        case 'C':
            print('Z',end='')
        case _:
            print(chr(ord(letter[i])-3),end='')

