price = int(input())

coins = [1,2,5,7]
SIZE = 10**9
calc = []

for _ in range(price + 1):
    calc.append(SIZE)

calc[0] = 0

for i in range(1,price+1):
    for j in coins:
        if (i - j >= 0):
            calc[i] = min(calc[i] ,calc[i-j] +1)
print(calc[price])