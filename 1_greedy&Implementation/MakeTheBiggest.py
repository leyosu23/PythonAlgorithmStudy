
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
