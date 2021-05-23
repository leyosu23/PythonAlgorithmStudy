'''
You want to repeatedly select one of the two procedures until any number of N is 1.
You can only choose when N is divided into K.

1.Subtract 1 from N
2. Divide N by K

Write a program to find the minimum number of times until N is 1 given N and K.
In the first row, N and K are given as natural numbers separated by spaces, respectively.
(1 <= N <= 100,000) (2<=K<=100,000)
'''

# Log O(n)

n,k = map(int, input().split())

cnt = 0

while True:
    target = (n // k) * k
    cnt += n - target
    n = target
    if n < k:
        break
    n //= k
    cnt += 1

cnt += (n - 1)
print(cnt)
