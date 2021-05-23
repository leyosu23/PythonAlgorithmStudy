# exchange algorithm when you have to exchange n while you have 4 kinds of coins
# O(n)
n = 1260
count = 0
array = [500,100,50,10]

for coin in array:
    count += n // coin
    n %= coin

print(count)