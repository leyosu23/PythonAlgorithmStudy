'''
When the integer N is given,
write a program that determines the number of all cases
in which any time of three is included, from 00:00:00 to N:59:59.

N is given in the first line as an integer (0 <= N <= 23)
'''
n = int(input())

cnt = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)
