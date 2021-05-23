'''
When each string S is given consisting of digits (only 0 to 9),
write a program, by putting an 'x' or '+' operator
between the digits to find the largest number that can be created.
However, all operations are done in order from the left, unlike the usual calculation method.
'''
data = input()
result = int(data[0])

i = 1
for i in range(1, len(data)):
    currentNum = int(data[i])
    if currentNum > 1 and result > 1:
        result *= currentNum
    else:
        result += currentNum
    i += 1

print(result)
