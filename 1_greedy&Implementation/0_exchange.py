'''
You are a clerk. There are 4 kinds of coins at the counter, which are 500,100,50,10.
Find the minimum number of coins to be exchanged , assuming the guest is paying N.
However, N is always a multiple of 10.
'''

# O(n)
n = 1260
count = 0
array = [500,100,50,10]

for coin in array:
    count += n // coin
    n %= coin

print(count)